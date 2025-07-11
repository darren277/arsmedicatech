"""
Appointment routes for scheduling functionality
"""
from flask import jsonify, request
from lib.services.auth_decorators import get_current_user, get_current_user_id
from lib.services.scheduling import SchedulingService
from lib.services.user_service import UserService
from lib.models.appointment import AppointmentStatus, AppointmentType


def create_appointment_route():
    """Create a new appointment"""
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Get current user
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        # Extract appointment data
        patient_id = data.get('patient_id')
        provider_id = data.get('provider_id', current_user.user_id)  # Default to current user if not specified
        appointment_date = data.get('appointment_date')
        start_time = data.get('start_time')
        end_time = data.get('end_time')
        appointment_type = data.get('appointment_type', 'consultation')
        notes = data.get('notes')
        location = data.get('location')
        
        # Validate required fields
        if not all([patient_id, appointment_date, start_time, end_time]):
            return jsonify({"error": "Missing required fields"}), 400
        
        # Create appointment
        scheduling_service = SchedulingService()
        scheduling_service.connect()
        try:
            success, message, appointment = scheduling_service.create_appointment(
                patient_id=patient_id,
                provider_id=provider_id,
                appointment_date=appointment_date,
                start_time=start_time,
                end_time=end_time,
                appointment_type=appointment_type,
                notes=notes,
                location=location
            )
            
            if success:
                return jsonify({
                    "success": True,
                    "message": message,
                    "appointment": {
                        "id": appointment.id,
                        "patient_id": appointment.patient_id,
                        "provider_id": appointment.provider_id,
                        "appointment_date": appointment.appointment_date,
                        "start_time": appointment.start_time,
                        "end_time": appointment.end_time,
                        "appointment_type": appointment.appointment_type,
                        "status": appointment.status,
                        "notes": appointment.notes,
                        "location": appointment.location,
                        "created_at": appointment.created_at
                    }
                }), 201
            else:
                return jsonify({"error": message}), 400
                
        finally:
            scheduling_service.close()
            
    except Exception as e:
        print(f"[ERROR] Error creating appointment: {e}")
        return jsonify({"error": "Internal server error"}), 500


def get_appointments_route():
    """Get appointments based on filters"""
    try:
        # Get current user
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        print(f"[DEBUG] Getting appointments for user: {current_user.user_id}, role: {current_user.role}")
        
        # Get query parameters
        date = request.args.get('date')
        patient_id = request.args.get('patient_id')
        provider_id = request.args.get('provider_id', current_user.user_id)
        status = request.args.get('status')
        
        print(f"[DEBUG] Query params - date: {date}, patient_id: {patient_id}, provider_id: {provider_id}, status: {status}")
        
        scheduling_service = SchedulingService()
        scheduling_service.connect()
        try:
            appointments = []
            
            # For debugging, get ALL appointments regardless of provider
            print("[DEBUG] Getting ALL appointments for debugging...")
            appointments = scheduling_service.get_all_appointments()
            print(f"[DEBUG] Found {len(appointments)} total appointments")
            
            # Filter by status if specified
            if status:
                appointments = [apt for apt in appointments if apt.status == status]
                print(f"[DEBUG] After status filter: {len(appointments)} appointments")
            
            # Convert to JSON-serializable format
            appointment_list = []
            for appointment in appointments:
                print(f"[DEBUG] Processing appointment: {appointment.id} - provider: {appointment.provider_id}, patient: {appointment.patient_id}")
                appointment_list.append({
                    "id": appointment.id,
                    "patient_id": appointment.patient_id,
                    "provider_id": appointment.provider_id,
                    "appointment_date": appointment.appointment_date,
                    "start_time": appointment.start_time,
                    "end_time": appointment.end_time,
                    "appointment_type": appointment.appointment_type,
                    "status": appointment.status,
                    "notes": appointment.notes,
                    "location": appointment.location,
                    "created_at": appointment.created_at,
                    "updated_at": appointment.updated_at
                })
            
            print(f"[DEBUG] Returning {len(appointment_list)} appointments")
            return jsonify({
                "success": True,
                "appointments": appointment_list,
                "total": len(appointment_list)
            }), 200
            
        finally:
            scheduling_service.close()
            
    except Exception as e:
        print(f"[ERROR] Error getting appointments: {e}")
        return jsonify({"error": "Internal server error"}), 500


def get_appointment_route(appointment_id):
    """Get a specific appointment"""
    try:
        # Get current user
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        scheduling_service = SchedulingService()
        scheduling_service.connect()
        try:
            appointment = scheduling_service.get_appointment(appointment_id)
            
            if not appointment:
                return jsonify({"error": "Appointment not found"}), 404
            
            # Check if user has access to this appointment
            if appointment.provider_id != current_user.user_id and appointment.patient_id != current_user.user_id:
                return jsonify({"error": "Access denied"}), 403
            
            return jsonify({
                "success": True,
                "appointment": {
                    "id": appointment.id,
                    "patient_id": appointment.patient_id,
                    "provider_id": appointment.provider_id,
                    "appointment_date": appointment.appointment_date,
                    "start_time": appointment.start_time,
                    "end_time": appointment.end_time,
                    "appointment_type": appointment.appointment_type,
                    "status": appointment.status,
                    "notes": appointment.notes,
                    "location": appointment.location,
                    "created_at": appointment.created_at,
                    "updated_at": appointment.updated_at
                }
            }), 200
            
        finally:
            scheduling_service.close()
            
    except Exception as e:
        print(f"[ERROR] Error getting appointment: {e}")
        return jsonify({"error": "Internal server error"}), 500


def update_appointment_route(appointment_id):
    """Update an appointment"""
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Get current user
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        scheduling_service = SchedulingService()
        scheduling_service.connect()
        try:
            # Get current appointment to check access
            appointment = scheduling_service.get_appointment(appointment_id)
            if not appointment:
                return jsonify({"error": "Appointment not found"}), 404
            
            # Check if user has access to this appointment
            if appointment.provider_id != current_user.user_id and appointment.patient_id != current_user.user_id:
                return jsonify({"error": "Access denied"}), 403
            
            # Update appointment
            success, message = scheduling_service.update_appointment(appointment_id, data)
            
            if success:
                return jsonify({
                    "success": True,
                    "message": message
                }), 200
            else:
                return jsonify({"error": message}), 400
                
        finally:
            scheduling_service.close()
            
    except Exception as e:
        print(f"[ERROR] Error updating appointment: {e}")
        return jsonify({"error": "Internal server error"}), 500


def cancel_appointment_route(appointment_id):
    """Cancel an appointment"""
    try:
        data = request.json or {}
        reason = data.get('reason')
        
        # Get current user
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        scheduling_service = SchedulingService()
        scheduling_service.connect()
        try:
            # Get current appointment to check access
            appointment = scheduling_service.get_appointment(appointment_id)
            if not appointment:
                return jsonify({"error": "Appointment not found"}), 404
            
            # Check if user has access to this appointment
            if appointment.provider_id != current_user.user_id and appointment.patient_id != current_user.user_id:
                return jsonify({"error": "Access denied"}), 403
            
            # Cancel appointment
            success, message = scheduling_service.cancel_appointment(appointment_id, reason)
            
            if success:
                return jsonify({
                    "success": True,
                    "message": message
                }), 200
            else:
                return jsonify({"error": message}), 400
                
        finally:
            scheduling_service.close()
            
    except Exception as e:
        print(f"[ERROR] Error cancelling appointment: {e}")
        return jsonify({"error": "Internal server error"}), 500


def confirm_appointment_route(appointment_id):
    """Confirm an appointment"""
    try:
        # Get current user
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        scheduling_service = SchedulingService()
        scheduling_service.connect()
        try:
            # Get current appointment to check access
            appointment = scheduling_service.get_appointment(appointment_id)
            if not appointment:
                return jsonify({"error": "Appointment not found"}), 404
            
            # Check if user has access to this appointment
            if appointment.provider_id != current_user.user_id and appointment.patient_id != current_user.user_id:
                return jsonify({"error": "Access denied"}), 403
            
            # Confirm appointment
            success, message = scheduling_service.confirm_appointment(appointment_id)
            
            if success:
                return jsonify({
                    "success": True,
                    "message": message
                }), 200
            else:
                return jsonify({"error": message}), 400
                
        finally:
            scheduling_service.close()
            
    except Exception as e:
        print(f"[ERROR] Error confirming appointment: {e}")
        return jsonify({"error": "Internal server error"}), 500


def get_available_slots_route():
    """Get available time slots for a provider on a specific date"""
    try:
        # Get current user
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        # Get query parameters
        date = request.args.get('date')
        provider_id = request.args.get('provider_id', current_user.user_id)
        duration = request.args.get('duration', 30, type=int)
        
        if not date:
            return jsonify({"error": "Date parameter is required"}), 400
        
        scheduling_service = SchedulingService()
        scheduling_service.connect()
        try:
            slots = scheduling_service.get_available_slots(provider_id, date, duration)
            
            return jsonify({
                "success": True,
                "date": date,
                "provider_id": provider_id,
                "duration_minutes": duration,
                "available_slots": slots
            }), 200
            
        finally:
            scheduling_service.close()
            
    except Exception as e:
        print(f"[ERROR] Error getting available slots: {e}")
        return jsonify({"error": "Internal server error"}), 500


def get_appointment_types_route():
    """Get available appointment types"""
    try:
        types = [
            {"value": "consultation", "label": "Consultation"},
            {"value": "follow_up", "label": "Follow-up"},
            {"value": "emergency", "label": "Emergency"},
            {"value": "routine", "label": "Routine Check-up"},
            {"value": "specialist", "label": "Specialist Visit"}
        ]
        
        return jsonify({
            "success": True,
            "appointment_types": types
        }), 200
        
    except Exception as e:
        print(f"[ERROR] Error getting appointment types: {e}")
        return jsonify({"error": "Internal server error"}), 500


def get_appointment_statuses_route():
    """Get available appointment statuses"""
    try:
        statuses = [
            {"value": "scheduled", "label": "Scheduled"},
            {"value": "confirmed", "label": "Confirmed"},
            {"value": "cancelled", "label": "Cancelled"},
            {"value": "completed", "label": "Completed"},
            {"value": "no_show", "label": "No Show"}
        ]
        
        return jsonify({
            "success": True,
            "appointment_statuses": statuses
        }), 200
        
    except Exception as e:
        print(f"[ERROR] Error getting appointment statuses: {e}")
        return jsonify({"error": "Internal server error"}), 500 