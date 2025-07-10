"""
Appointment model for scheduling functionality
"""
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, List
from enum import Enum


class AppointmentStatus(Enum):
    SCHEDULED = "scheduled"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"
    COMPLETED = "completed"
    NO_SHOW = "no_show"


class AppointmentType(Enum):
    CONSULTATION = "consultation"
    FOLLOW_UP = "follow_up"
    EMERGENCY = "emergency"
    ROUTINE = "routine"
    SPECIALIST = "specialist"


class Appointment:
    def __init__(self, 
                 patient_id: str,
                 provider_id: str,
                 appointment_date: str,
                 start_time: str,
                 end_time: str,
                 appointment_type: str = "consultation",
                 status: str = "scheduled",
                 notes: str = None,
                 location: str = None,
                 id: str = None,
                 created_at: str = None,
                 updated_at: str = None):
        """
        Initialize an Appointment object
        
        :param patient_id: ID of the patient
        :param provider_id: ID of the healthcare provider
        :param appointment_date: Date of appointment (YYYY-MM-DD)
        :param start_time: Start time (HH:MM)
        :param end_time: End time (HH:MM)
        :param appointment_type: Type of appointment
        :param status: Current status of appointment
        :param notes: Additional notes
        :param location: Location of appointment
        :param id: Database record ID
        :param created_at: Creation timestamp
        :param updated_at: Last update timestamp
        """
        self.patient_id = patient_id
        self.provider_id = provider_id
        self.appointment_date = appointment_date
        self.start_time = start_time
        self.end_time = end_time
        self.appointment_type = appointment_type
        self.status = status
        self.notes = notes or ""
        self.location = location or ""
        self.id = id
        self.created_at = created_at or datetime.utcnow().isoformat()
        self.updated_at = updated_at or datetime.utcnow().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert appointment to dictionary for database storage"""
        return {
            'patient_id': self.patient_id,
            'provider_id': self.provider_id,
            'appointment_date': self.appointment_date,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'appointment_type': self.appointment_type,
            'status': self.status,
            'notes': self.notes,
            'location': self.location,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Appointment':
        """Create appointment from dictionary"""
        # Convert RecordID to string if it exists
        appointment_id = data.get('id')
        if hasattr(appointment_id, '__str__'):
            appointment_id = str(appointment_id)
        
        return cls(
            patient_id=data.get('patient_id'),
            provider_id=data.get('provider_id'),
            appointment_date=data.get('appointment_date'),
            start_time=data.get('start_time'),
            end_time=data.get('end_time'),
            appointment_type=data.get('appointment_type', 'consultation'),
            status=data.get('status', 'scheduled'),
            notes=data.get('notes'),
            location=data.get('location'),
            id=appointment_id,
            created_at=data.get('created_at'),
            updated_at=data.get('updated_at')
        )
    
    def get_duration_minutes(self) -> int:
        """Calculate appointment duration in minutes"""
        try:
            start = datetime.strptime(self.start_time, '%H:%M')
            end = datetime.strptime(self.end_time, '%H:%M')
            duration = end - start
            return int(duration.total_seconds() / 60)
        except ValueError:
            return 0
    
    def is_confirmed(self) -> bool:
        """Check if appointment is confirmed"""
        return self.status == AppointmentStatus.CONFIRMED.value
    
    def is_cancelled(self) -> bool:
        """Check if appointment is cancelled"""
        return self.status == AppointmentStatus.CANCELLED.value
    
    def is_completed(self) -> bool:
        """Check if appointment is completed"""
        return self.status == AppointmentStatus.COMPLETED.value
    
    def can_be_cancelled(self) -> bool:
        """Check if appointment can be cancelled"""
        return self.status in [
            AppointmentStatus.SCHEDULED.value,
            AppointmentStatus.CONFIRMED.value
        ]
    
    def get_datetime(self) -> datetime:
        """Get full datetime of appointment start"""
        try:
            date_obj = datetime.strptime(self.appointment_date, '%Y-%m-%d')
            time_obj = datetime.strptime(self.start_time, '%H:%M').time()
            return datetime.combine(date_obj.date(), time_obj)
        except ValueError:
            return None
    
    def is_in_past(self) -> bool:
        """Check if appointment is in the past"""
        appointment_dt = self.get_datetime()
        if not appointment_dt:
            return False
        return appointment_dt < datetime.now()
    
    def is_today(self) -> bool:
        """Check if appointment is today"""
        appointment_dt = self.get_datetime()
        if not appointment_dt:
            return False
        return appointment_dt.date() == datetime.now().date()
    
    def is_this_week(self) -> bool:
        """Check if appointment is this week"""
        appointment_dt = self.get_datetime()
        if not appointment_dt:
            return False
        today = datetime.now()
        week_start = today - timedelta(days=today.weekday())
        week_end = week_start + timedelta(days=6)
        return week_start.date() <= appointment_dt.date() <= week_end.date()
    
    def schema(self):
        """Define database schema for appointments"""
        statements = []
        statements.append('DEFINE TABLE appointment SCHEMAFULL;')
        statements.append('DEFINE FIELD patient_id ON appointment TYPE record<patient> ASSERT $value != none;')
        statements.append('DEFINE FIELD provider_id ON appointment TYPE record<user> ASSERT $value != none;')
        statements.append('DEFINE FIELD appointment_date ON appointment TYPE string ASSERT $value != none;')
        statements.append('DEFINE FIELD start_time ON appointment TYPE string ASSERT $value != none;')
        statements.append('DEFINE FIELD end_time ON appointment TYPE string ASSERT $value != none;')
        statements.append('DEFINE FIELD appointment_type ON appointment TYPE string;')
        statements.append('DEFINE FIELD status ON appointment TYPE string;')
        statements.append('DEFINE FIELD notes ON appointment TYPE string;')
        statements.append('DEFINE FIELD location ON appointment TYPE string;')
        statements.append('DEFINE FIELD created_at ON appointment TYPE string;')
        statements.append('DEFINE FIELD updated_at ON appointment TYPE string;')
        
        # Indexes for efficient querying
        statements.append('DEFINE INDEX idx_appointment_date ON appointment FIELDS appointment_date;')
        statements.append('DEFINE INDEX idx_appointment_provider ON appointment FIELDS provider_id;')
        statements.append('DEFINE INDEX idx_appointment_patient ON appointment FIELDS patient_id;')
        statements.append('DEFINE INDEX idx_appointment_status ON appointment FIELDS status;')
        statements.append('DEFINE INDEX idx_appointment_datetime ON appointment FIELDS appointment_date, start_time;')
        
        return statements 