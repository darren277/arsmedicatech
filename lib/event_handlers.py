"""
Event handlers for webhook delivery
"""


from lib.events import (
    AppointmentCreated,
    AppointmentUpdated,
    AppointmentCancelled,
    AppointmentConfirmed,
    AppointmentCompleted
)
from lib.infra.event_bus import event_bus
from lib.tasks import deliver_webhooks
from settings import logger


def on_appointment_created(event: AppointmentCreated) -> None:
    """
    Handle appointment created event by triggering webhook delivery
    
    :param event: AppointmentCreated event
    """
    logger.debug(f"Handling appointment created event: {event.appointment_id}")
    
    payload = {
        "appointment_id": event.appointment_id,
        "patient_id": event.patient_id,
        "provider_id": event.provider_id,
        "appointment_date": event.appointment_date,
        "start_time": event.start_time,
        "end_time": event.end_time,
        "appointment_type": event.appointment_type,
        "timestamp": event.occurred_at.isoformat()
    }
    
    # Trigger webhook delivery in background
    deliver_webhooks("appointment.created", payload)


def on_appointment_updated(event: AppointmentUpdated) -> None:
    """
    Handle appointment updated event by triggering webhook delivery
    
    :param event: AppointmentUpdated event
    """
    logger.debug(f"Handling appointment updated event: {event.appointment_id}")
    
    payload = {
        "appointment_id": event.appointment_id,
        "patient_id": event.patient_id,
        "provider_id": event.provider_id,
        "appointment_date": event.appointment_date,
        "start_time": event.start_time,
        "end_time": event.end_time,
        "appointment_type": event.appointment_type,
        "status": event.status,
        "changes": event.changes,
        "timestamp": event.occurred_at.isoformat()
    }
    
    # Trigger webhook delivery in background
    deliver_webhooks("appointment.updated", payload)


def on_appointment_cancelled(event: AppointmentCancelled) -> None:
    """
    Handle appointment cancelled event by triggering webhook delivery
    
    :param event: AppointmentCancelled event
    """
    logger.debug(f"Handling appointment cancelled event: {event.appointment_id}")
    
    payload = {
        "appointment_id": event.appointment_id,
        "patient_id": event.patient_id,
        "provider_id": event.provider_id,
        "reason": event.reason,
        "timestamp": event.occurred_at.isoformat()
    }
    
    # Trigger webhook delivery in background
    deliver_webhooks("appointment.cancelled", payload)


def on_appointment_confirmed(event: AppointmentConfirmed) -> None:
    """
    Handle appointment confirmed event by triggering webhook delivery
    
    :param event: AppointmentConfirmed event
    """
    logger.debug(f"Handling appointment confirmed event: {event.appointment_id}")
    
    payload = {
        "appointment_id": event.appointment_id,
        "patient_id": event.patient_id,
        "provider_id": event.provider_id,
        "timestamp": event.occurred_at.isoformat()
    }
    
    # Trigger webhook delivery in background
    deliver_webhooks("appointment.confirmed", payload)


def on_appointment_completed(event: AppointmentCompleted) -> None:
    """
    Handle appointment completed event by triggering webhook delivery
    
    :param event: AppointmentCompleted event
    """
    logger.debug(f"Handling appointment completed event: {event.appointment_id}")
    
    payload = {
        "appointment_id": event.appointment_id,
        "patient_id": event.patient_id,
        "provider_id": event.provider_id,
        "timestamp": event.occurred_at.isoformat()
    }
    
    # Trigger webhook delivery in background
    deliver_webhooks("appointment.completed", payload)


def register_event_handlers() -> None:
    """
    Register all event handlers with the event bus
    """
    logger.info("Registering event handlers for webhook delivery")
    
    event_bus.subscribe(AppointmentCreated, on_appointment_created)
    event_bus.subscribe(AppointmentUpdated, on_appointment_updated)
    event_bus.subscribe(AppointmentCancelled, on_appointment_cancelled)
    event_bus.subscribe(AppointmentConfirmed, on_appointment_confirmed)
    event_bus.subscribe(AppointmentCompleted, on_appointment_completed)
    
    logger.info("Event handlers registered successfully")
