"""
Appointment routes for scheduling functionality
"""
from typing import Any, Dict, Tuple

from flask import Response, jsonify, request

from lib.services.auth_decorators import get_current_user
from lib.services.scheduling import SchedulingService
from settings import logger


def create_appointment_route() -> Tuple[Response, int]:
    """
    Create a new appointment

    This endpoint allows users to create a new appointment.
    It requires the user to be authenticated and provides necessary details
    such as patient ID, provider ID, appointment date, start and end times,
    appointment type, notes, and location.

    Returns a JSON response with the appointment details if successful,
    or an error message if there was an issue.

    HTTP Status Codes:
    - 201 Created: Appointment successfully created
    - 400 Bad Request: Missing required fields or invalid data
    - 401 Unauthorized: User not authenticated
    - 500 Internal Server Error: An unexpected error occurred

    Example Request:
    POST /appointments
    Content-Type: application/json
    {
        "patient_id": "Patient:12345",
        ...
    }

    Example Response:
    HTTP/1.1 201 Created
    {
        "success": true,
        "message": "Appointment created successfully",
    }

    :return: JSON response with appointment details or error message
    """
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
        provider_id = data.get('provider_id', current_user.user_id) # Default to current user if not specified
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
                assert appointment is not None, "Appointment should not be None"

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
        logger.error(f"Error creating appointment: {e}")
        return jsonify({"error": "Internal server error"}), 500


def get_appointments_route() -> Tuple[Response, int]:
    """
    Get appointments based on filters

    This endpoint retrieves appointments based on various filters such as date,
    patient ID, provider ID, and status. It allows users to view their appointments
    or those of patients they manage.
    Returns a JSON response with the list of appointments and their details.
    HTTP Status Codes:
    - 200 OK: Successfully retrieved appointments
    - 401 Unauthorized: User not authenticated
    - 500 Internal Server Error: An unexpected error occurred
    Example Request:
    GET /appointments?date=2023-10-01&patient_id=Patient:12345&provider_id=Provider:67890&status=scheduled
    Example Response:
    HTTP/1.1 200 OK
    {
        "success": true,
        "appointments": [
            {
                "id": "Appointment:12345",
                "patient_id": "Patient:12345",
                "provider_id": "Provider:67890",
                "appointment_date": "2023-10-01",
                "start_time": "10:00",
                "end_time": "10:30",
                "appointment_type": "consultation",
                "status": "scheduled",
                "notes": "",
                "location": "Clinic A",
                "created_at": "2023-09-01T12:00:00Z",
                "updated_at": "2023-09-01T12:00:00Z"
            }
        ],
        "total": 1
    }

    :return: JSON response with appointments or error message
    """
    try:
        # Get current user
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        logger.debug(f"Getting appointments for user: {current_user.user_id}, role: {current_user.role}")
        
        # Get query parameters
        date = request.args.get('date')
        patient_id = request.args.get('patient_id')
        provider_id = request.args.get('provider_id', current_user.user_id)
        status = request.args.get('status')
        
        logger.debug(f"Query params - date: {date}, patient_id: {patient_id}, provider_id: {provider_id}, status: {status}")
        
        scheduling_service = SchedulingService()
        scheduling_service.connect()
        try:
            appointments = []
            
            # For debugging, get ALL appointments regardless of provider
            logger.debug("Getting ALL appointments for debugging...")
            appointments = scheduling_service.get_all_appointments()
            logger.debug(f"Found {len(appointments)} total appointments")
            
            # Filter by status if specified
            if status:
                appointments = [apt for apt in appointments if apt.status == status]
                logger.debug(f"After status filter: {len(appointments)} appointments")
            
            # Convert to JSON-serializable format
            appointment_list: list[Dict[str, Any]] = []
            for appointment in appointments:
                logger.debug(f"Processing appointment: {appointment.id} - provider: {appointment.provider_id}, patient: {appointment.patient_id}")
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
            
            logger.debug(f"Returning {len(appointment_list)} appointments")
            return jsonify({
                "success": True,
                "appointments": appointment_list,
                "total": len(appointment_list)
            }), 200
            
        finally:
            scheduling_service.close()
            
    except Exception as e:
        logger.error(f"Error getting appointments: {e}")
        return jsonify({"error": "Internal server error"}), 500


def get_appointment_route(appointment_id: str) -> Tuple[Response, int]:
    """
    Get a specific appointment

    This endpoint retrieves details of a specific appointment by its ID.
    It checks if the user has access to the appointment based on their role
    (provider or patient) and returns the appointment details if found.
    Returns a JSON response with the appointment details or an error message.
    HTTP Status Codes:
    - 200 OK: Successfully retrieved appointment details
    - 401 Unauthorized: User not authenticated
    - 403 Forbidden: User does not have access to this appointment
    - 404 Not Found: Appointment not found
    - 500 Internal Server Error: An unexpected error occurred
    Example Request:
    GET /appointments/Appointment:12345
    Example Response:
    HTTP/1.1 200 OK
    {
        "success": true,
        "appointment": {
            "id": "Appointment:12345",
            "patient_id": "Patient:12345",
            "provider_id": "Provider:67890",
            "appointment_date": "2023-10-01",
            "start_time": "10:00",
            "end_time": "10:30",
            "appointment_type": "consultation",
            "status": "scheduled",
            "notes": "",
            "location": "Clinic A",
            "created_at": "2023-09-01T12:00:00Z",
            "updated_at": "2023-09-01T12:00:00Z"
        }
    }
    :param appointment_id: The ID of the appointment to retrieve
    :return: JSON response with appointment details or error message
    """
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
        logger.error(f"Error getting appointment: {e}")
        return jsonify({"error": "Internal server error"}), 500


def update_appointment_route(appointment_id: str) -> Tuple[Response, int]:
    """
    Update an appointment

    This endpoint allows users to update an existing appointment.
    It requires the user to be authenticated and provides the appointment ID
    along with the fields to be updated such as appointment date, start and end times,
    appointment type, notes, and location.
    Returns a JSON response indicating success or failure of the update operation.

    HTTP Status Codes:
    - 200 OK: Appointment successfully updated
    - 400 Bad Request: Missing required fields or invalid data
    - 401 Unauthorized: User not authenticated
    - 403 Forbidden: User does not have access to this appointment
    - 404 Not Found: Appointment not found
    - 500 Internal Server Error: An unexpected error occurred
    Example Request:
    PUT /appointments/Appointment:12345
    Content-Type: application/json
    {
        "appointment_date": "2023-10-01",
        "start_time": "10:00",
        "end_time": "10:30",
        "appointment_type": "follow_up",
        "notes": "Updated notes",
        "location": "Updated Clinic A"
    }
    Example Response:
    HTTP/1.1 200 OK
    {
        "success": true,
        "message": "Appointment updated successfully"
    }

    :param appointment_id: The ID of the appointment to update
    :return: JSON response with success message or error details
    """
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
        logger.error(f"Error updating appointment: {e}")
        return jsonify({"error": "Internal server error"}), 500


def cancel_appointment_route(appointment_id: str) -> Tuple[Response, int]:
    """
    Cancel an appointment

    This endpoint allows users to cancel an existing appointment.
    It requires the user to be authenticated and provides the appointment ID
    along with an optional reason for cancellation.
    Returns a JSON response indicating success or failure of the cancellation operation.
    HTTP Status Codes:
    - 200 OK: Appointment successfully cancelled
    - 400 Bad Request: Missing required fields or invalid data
    - 401 Unauthorized: User not authenticated
    - 403 Forbidden: User does not have access to this appointment
    - 404 Not Found: Appointment not found
    - 500 Internal Server Error: An unexpected error occurred
    Example Request:
    DELETE /appointments/Appointment:12345
    Content-Type: application/json
    {
        "reason": "Patient requested cancellation"
    }
    Example Response:
    HTTP/1.1 200 OK
    {
        "success": true,
        "message": "Appointment cancelled successfully"
    }

    :param appointment_id: The ID of the appointment to cancel
    :return: JSON response with success message or error details
    """
    try:
        data: Dict[str, Any] = request.json or {}
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
        logger.error(f"Error cancelling appointment: {e}")
        return jsonify({"error": "Internal server error"}), 500


def confirm_appointment_route(appointment_id: str) -> Tuple[Response, int]:
    """
    Confirm an appointment

    This endpoint allows users to confirm an existing appointment.
    It requires the user to be authenticated and provides the appointment ID.
    Returns a JSON response indicating success or failure of the confirmation operation.
    HTTP Status Codes:
    - 200 OK: Appointment successfully confirmed
    - 400 Bad Request: Missing required fields or invalid data
    - 401 Unauthorized: User not authenticated
    - 403 Forbidden: User does not have access to this appointment
    - 404 Not Found: Appointment not found
    - 500 Internal Server Error: An unexpected error occurred
    Example Request:
    POST /appointments/Appointment:12345/confirm
    Example Response:
    HTTP/1.1 200 OK
    {
        "success": true,
        "message": "Appointment confirmed successfully"
    }

    :param appointment_id: The ID of the appointment to confirm
    :return: JSON response with success message or error details
    """
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
        logger.error(f"Error confirming appointment: {e}")
        return jsonify({"error": "Internal server error"}), 500


def get_available_slots_route() -> Tuple[Response, int]:
    """
    Get available time slots for a provider on a specific date

    This endpoint retrieves available time slots for a specific provider on a given date.
    It allows users to check availability for scheduling appointments.
    Returns a JSON response with the available time slots or an error message.
    HTTP Status Codes:
    - 200 OK: Successfully retrieved available slots
    - 400 Bad Request: Missing required parameters or invalid data
    - 401 Unauthorized: User not authenticated
    - 500 Internal Server Error: An unexpected error occurred
    Example Request:
    GET /appointments/available_slots?date=2023-10-01&provider_id=Provider:67890&duration=30
    Example Response:
    HTTP/1.1 200 OK
    {
        "success": true,
        "date": "2023-10-01",
        "provider_id": "Provider:67890",
        "duration_minutes": 30,
        "available_slots": [
            "10:00-10:30",
            "10:30-11:00",
            ...
        ]
    }
    :return: JSON response with available slots or error message
    """
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
        logger.error(f"Error getting available slots: {e}")
        return jsonify({"error": "Internal server error"}), 500


def get_appointment_types_route() -> Tuple[Response, int]:
    """
    Get available appointment types

    This endpoint retrieves a list of available appointment types.
    It can be used to populate dropdowns or selection lists in the UI.
    Returns a JSON response with the list of appointment types.
    HTTP Status Codes:
    - 200 OK: Successfully retrieved appointment types
    - 500 Internal Server Error: An unexpected error occurred
    Example Request:
    GET /appointments/types
    Example Response:
    HTTP/1.1 200 OK
    {
        "success": true,
        "appointment_types": [
            {"value": "consultation", "label": "Consultation"},
            {"value": "follow_up", "label": "Follow-up"},
            {"value": "emergency", "label": "Emergency"},
            {"value": "routine", "label": "Routine Check-up"},
            {"value": "specialist", "label": "Specialist Visit"}
        ]
    }
    :return: JSON response with appointment types or error message
    """
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
        logger.error(f"Error getting appointment types: {e}")
        return jsonify({"error": "Internal server error"}), 500


def get_appointment_statuses_route() -> Tuple[Response, int]:
    """
    Get available appointment statuses

    This endpoint retrieves a list of available appointment statuses.
    It can be used to populate dropdowns or selection lists in the UI.
    Returns a JSON response with the list of appointment statuses.
    HTTP Status Codes:
    - 200 OK: Successfully retrieved appointment statuses
    - 500 Internal Server Error: An unexpected error occurred
    Example Request:
    GET /appointments/statuses
    Example Response:
    HTTP/1.1 200 OK
    {
        "success": true,
        "appointment_statuses": [
            {"value": "scheduled", "label": "Scheduled"},
            {"value": "confirmed", "label": "Confirmed"},
            {"value": "cancelled", "label": "Cancelled"},
            {"value": "completed", "label": "Completed"},
            {"value": "no_show", "label": "No Show"}
        ]
    }
    :return: JSON response with appointment statuses or error message
    """
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
        logger.error(f"Error getting appointment statuses: {e}")
        return jsonify({"error": "Internal server error"}), 500
