"""
Domain events for webhook system
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any


@dataclass
class AppointmentCreated:
    """Raised after an appointment is successfully created in the database."""
    appointment_id: str
    patient_id: str
    provider_id: str
    appointment_date: str
    start_time: str
    end_time: str
    appointment_type: str
    occurred_at: datetime


@dataclass
class AppointmentUpdated:
    """Raised after an appointment is successfully updated in the database."""
    appointment_id: str
    patient_id: str
    provider_id: str
    appointment_date: str
    start_time: str
    end_time: str
    appointment_type: str
    status: str
    changes: Dict[str, Any]
    occurred_at: datetime


@dataclass
class AppointmentCancelled:
    """Raised after an appointment is successfully cancelled."""
    appointment_id: str
    patient_id: str
    provider_id: str
    reason: Optional[str]
    occurred_at: datetime


@dataclass
class AppointmentConfirmed:
    """Raised after an appointment is successfully confirmed."""
    appointment_id: str
    patient_id: str
    provider_id: str
    occurred_at: datetime


@dataclass
class AppointmentCompleted:
    """Raised after an appointment is marked as completed."""
    appointment_id: str
    patient_id: str
    provider_id: str
    occurred_at: datetime 