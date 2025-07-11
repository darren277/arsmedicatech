"""
Scheduling service for managing appointments
"""
from datetime import datetime, timedelta
from typing import List, Optional, Tuple, Dict, Any
from lib.db.surreal import DbController
from lib.models.appointment import Appointment, AppointmentStatus, AppointmentType


class SchedulingService:
    def __init__(self):
        self.db = DbController()
    
    def connect(self):
        """Connect to database"""
        self.db.connect()
    
    def close(self):
        """Close database connection"""
        self.db.close()
    
    def create_appointment(self, 
                          patient_id: str,
                          provider_id: str,
                          appointment_date: str,
                          start_time: str,
                          end_time: str,
                          appointment_type: str = "consultation",
                          notes: str = None,
                          location: str = None) -> Tuple[bool, str, Optional[Appointment]]:
        """
        Create a new appointment
        
        :return: (success, message, appointment)
        """
        try:
            # Validate inputs
            if not all([patient_id, provider_id, appointment_date, start_time, end_time]):
                return False, "Missing required fields", None
            
            # Validate date format
            try:
                datetime.strptime(appointment_date, '%Y-%m-%d')
            except ValueError:
                return False, "Invalid date format. Use YYYY-MM-DD", None
            
            # Validate time format
            try:
                datetime.strptime(start_time, '%H:%M')
                datetime.strptime(end_time, '%H:%M')
            except ValueError:
                return False, "Invalid time format. Use HH:MM", None
            
            # Check for time conflicts
            conflict = self._check_time_conflict(provider_id, appointment_date, start_time, end_time)
            if conflict:
                return False, f"Time conflict: {conflict}", None
            
            # Create appointment
            appointment = Appointment(
                patient_id=patient_id,
                provider_id=provider_id,
                appointment_date=appointment_date,
                start_time=start_time,
                end_time=end_time,
                appointment_type=appointment_type,
                notes=notes,
                location=location
            )
            
            # Save to database
            result = self.db.create('appointment', appointment.to_dict())
            if result:
                appointment.id = result.get('id')
                return True, "Appointment created successfully", appointment
            else:
                return False, "Failed to create appointment", None
                
        except Exception as e:
            return False, f"Error creating appointment: {str(e)}", None
    
    def get_appointment(self, appointment_id: str) -> Optional[Appointment]:
        """Get appointment by ID"""
        try:
            result = self.db.get('appointment', appointment_id)
            if result:
                return Appointment.from_dict(result)
            return None
        except Exception as e:
            print(f"Error getting appointment: {e}")
            return None
    
    def get_appointments_by_date(self, date: str, provider_id: str = None) -> List[Appointment]:
        """Get appointments for a specific date"""
        try:
            query = "SELECT * FROM appointment WHERE appointment_date = $date"
            params = {"date": date}
            
            if provider_id:
                query += " AND provider_id = $provider_id"
                params["provider_id"] = provider_id
            
            query += " ORDER BY start_time"
            
            results = self.db.query(query, params)
            appointments = []
            
            for result in results:
                if result.get('result'):
                    for record in result['result']:
                        appointments.append(Appointment.from_dict(record))
            
            return appointments
        except Exception as e:
            print(f"Error getting appointments by date: {e}")
            return []
    
    def get_appointments_by_patient(self, patient_id: str) -> List[Appointment]:
        """Get all appointments for a patient"""
        try:
            query = """
                SELECT * FROM appointment 
                WHERE patient_id = $patient_id 
                ORDER BY appointment_date DESC, start_time DESC
            """
            results = self.db.query(query, {"patient_id": patient_id})
            appointments = []
            
            for result in results:
                if result.get('result'):
                    for record in result['result']:
                        appointments.append(Appointment.from_dict(record))
            
            return appointments
        except Exception as e:
            print(f"Error getting appointments by patient: {e}")
            return []
    
    def get_appointments_by_provider(self, provider_id: str, start_date: str = None, end_date: str = None) -> List[Appointment]:
        """Get appointments for a provider within a date range"""
        try:
            query = "SELECT * FROM appointment WHERE provider_id = $provider_id"
            params = {"provider_id": provider_id}
            
            if start_date and end_date:
                query += " AND appointment_date >= $start_date AND appointment_date <= $end_date"
                params["start_date"] = start_date
                params["end_date"] = end_date
            
            query += " ORDER BY appointment_date, start_time"
            
            results = self.db.query(query, params)
            appointments = []
            
            for result in results:
                if result.get('result'):
                    for record in result['result']:
                        appointments.append(Appointment.from_dict(record))
            
            return appointments
        except Exception as e:
            print(f"Error getting appointments by provider: {e}")
            return []
    
    def get_all_appointments(self) -> List[Appointment]:
        """Get all appointments (for debugging)"""
        try:
            print("[DEBUG] get_all_appointments: Starting query...")
            
            # First, let's see what tables exist
            print("[DEBUG] Checking what tables exist...")
            tables_query = "INFO FOR DB"
            tables_result = self.db.query(tables_query, {})
            print(f"[DEBUG] Tables query result: {tables_result}")
            
            # Try a simple query to see what's in the appointment table
            print("[DEBUG] Trying simple SELECT query...")
            simple_query = "SELECT * FROM appointment"
            simple_result = self.db.query(simple_query, {})
            print(f"[DEBUG] Simple query result: {simple_result}")
            
            # Now try the full query
            query = "SELECT * FROM appointment ORDER BY appointment_date, start_time"
            print(f"[DEBUG] Executing query: {query}")
            results = self.db.query(query, {})
            print(f"[DEBUG] Full query results: {results}")
            
            appointments = []
            
            for result in results:
                print(f"[DEBUG] Processing result: {result}")
                # The result is already the record, not nested under 'result'
                if isinstance(result, dict):
                    print(f"[DEBUG] Processing record: {result}")
                    appointments.append(Appointment.from_dict(result))
                elif result.get('result'):
                    # Fallback for nested structure
                    for record in result['result']:
                        print(f"[DEBUG] Processing nested record: {record}")
                        appointments.append(Appointment.from_dict(record))
            
            print(f"[DEBUG] Final appointments list: {appointments}")
            return appointments
        except Exception as e:
            print(f"Error getting all appointments: {e}")
            import traceback
            print(f"[ERROR] Traceback: {traceback.format_exc()}")
            return []
    
    def update_appointment(self, appointment_id: str, updates: Dict[str, Any]) -> Tuple[bool, str]:
        """Update an appointment"""
        try:
            # Get current appointment
            appointment = self.get_appointment(appointment_id)
            if not appointment:
                return False, "Appointment not found"
            
            # Check for time conflicts if time is being updated
            if 'start_time' in updates or 'end_time' in updates or 'appointment_date' in updates:
                new_date = updates.get('appointment_date', appointment.appointment_date)
                new_start = updates.get('start_time', appointment.start_time)
                new_end = updates.get('end_time', appointment.end_time)
                
                conflict = self._check_time_conflict(
                    appointment.provider_id, 
                    new_date, 
                    new_start, 
                    new_end, 
                    exclude_id=appointment_id
                )
                if conflict:
                    return False, f"Time conflict: {conflict}"
            
            # Update fields
            for key, value in updates.items():
                if hasattr(appointment, key):
                    setattr(appointment, key, value)
            
            appointment.updated_at = datetime.utcnow().isoformat()
            
            # Save to database
            result = self.db.update('appointment', appointment_id, appointment.to_dict())
            if result:
                return True, "Appointment updated successfully"
            else:
                return False, "Failed to update appointment"
                
        except Exception as e:
            return False, f"Error updating appointment: {str(e)}"
    
    def cancel_appointment(self, appointment_id: str, reason: str = None) -> Tuple[bool, str]:
        """Cancel an appointment"""
        try:
            appointment = self.get_appointment(appointment_id)
            if not appointment:
                return False, "Appointment not found"
            
            if not appointment.can_be_cancelled():
                return False, "Appointment cannot be cancelled"
            
            updates = {
                'status': AppointmentStatus.CANCELLED.value,
                'notes': f"{appointment.notes}\n\nCancelled: {reason or 'No reason provided'}"
            }
            
            return self.update_appointment(appointment_id, updates)
            
        except Exception as e:
            return False, f"Error cancelling appointment: {str(e)}"
    
    def confirm_appointment(self, appointment_id: str) -> Tuple[bool, str]:
        """Confirm an appointment"""
        try:
            appointment = self.get_appointment(appointment_id)
            if not appointment:
                return False, "Appointment not found"
            
            if appointment.status != AppointmentStatus.SCHEDULED.value:
                return False, "Appointment is not in scheduled status"
            
            updates = {'status': AppointmentStatus.CONFIRMED.value}
            return self.update_appointment(appointment_id, updates)
            
        except Exception as e:
            return False, f"Error confirming appointment: {str(e)}"
    
    def complete_appointment(self, appointment_id: str) -> Tuple[bool, str]:
        """Mark appointment as completed"""
        try:
            appointment = self.get_appointment(appointment_id)
            if not appointment:
                return False, "Appointment not found"
            
            if appointment.status not in [AppointmentStatus.SCHEDULED.value, AppointmentStatus.CONFIRMED.value]:
                return False, "Appointment cannot be marked as completed"
            
            updates = {'status': AppointmentStatus.COMPLETED.value}
            return self.update_appointment(appointment_id, updates)
            
        except Exception as e:
            return False, f"Error completing appointment: {str(e)}"
    
    def get_available_slots(self, provider_id: str, date: str, duration_minutes: int = 30) -> List[Dict[str, str]]:
        """Get available time slots for a provider on a specific date"""
        try:
            # Get existing appointments for the date
            appointments = self.get_appointments_by_date(date, provider_id)
            
            # Define business hours (9 AM to 5 PM)
            business_start = datetime.strptime('09:00', '%H:%M')
            business_end = datetime.strptime('17:00', '%H:%M')
            
            # Create time slots
            slots = []
            current_time = business_start
            
            while current_time + timedelta(minutes=duration_minutes) <= business_end:
                slot_start = current_time.strftime('%H:%M')
                slot_end = (current_time + timedelta(minutes=duration_minutes)).strftime('%H:%M')
                
                # Check if slot conflicts with existing appointments
                conflict = False
                for appointment in appointments:
                    if self._times_overlap(slot_start, slot_end, appointment.start_time, appointment.end_time):
                        conflict = True
                        break
                
                if not conflict:
                    slots.append({
                        'start_time': slot_start,
                        'end_time': slot_end
                    })
                
                current_time += timedelta(minutes=30)  # 30-minute intervals
            
            return slots
            
        except Exception as e:
            print(f"Error getting available slots: {e}")
            return []
    
    def _check_time_conflict(self, provider_id: str, date: str, start_time: str, end_time: str, exclude_id: str = None) -> Optional[str]:
        """Check for time conflicts with existing appointments"""
        try:
            appointments = self.get_appointments_by_date(date, provider_id)
            
            for appointment in appointments:
                if exclude_id and appointment.id == exclude_id:
                    continue
                
                if appointment.status in [AppointmentStatus.CANCELLED.value, AppointmentStatus.COMPLETED.value]:
                    continue
                
                if self._times_overlap(start_time, end_time, appointment.start_time, appointment.end_time):
                    return f"Conflicts with appointment at {appointment.start_time}-{appointment.end_time}"
            
            return None
            
        except Exception as e:
            print(f"Error checking time conflict: {e}")
            return "Error checking availability"
    
    def _times_overlap(self, start1: str, end1: str, start2: str, end2: str) -> bool:
        """Check if two time ranges overlap"""
        try:
            s1 = datetime.strptime(start1, '%H:%M')
            e1 = datetime.strptime(end1, '%H:%M')
            s2 = datetime.strptime(start2, '%H:%M')
            e2 = datetime.strptime(end2, '%H:%M')
            
            return s1 < e2 and s2 < e1
        except ValueError:
            return False
