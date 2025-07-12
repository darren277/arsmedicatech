"""
Routes for patient and encounter management in a healthcare application.
"""
from typing import Tuple

from flask import request, jsonify, Response

from lib.models.patient import update_patient, search_patient_history, get_patient_by_id, delete_patient, \
    get_all_patients, create_patient, get_all_encounters, get_encounters_by_patient, get_encounter_by_id, \
    create_encounter, update_encounter, delete_encounter, search_encounter_history
from lib.data_types import PatientID
from settings import logger


def patch_intake_route(patient_id: PatientID) -> Tuple[Response, int]:
    """
    API endpoint to patch a patient's intake data.
    :param patient_id: The ID of the patient to update, formatted as 'Patient:{patient_id}'.
    :return: Response indicating success or failure.
    """
    payload = request.get_json()
    logger.debug(f"Patching patient {patient_id} with payload: {payload}")

    # Map 'User:' to patient ID if needed
    patient_id = patient_id.replace('User:', '')

    result = update_patient(patient_id, payload)
    logger.debug(f"Update result: {result}")
    if not result:
        logger.error(f"Failed to update patient {patient_id}: {result}")
        return jsonify({"error": "Failed to update patient"}), 400
    return jsonify({'ok': True}), 200


def search_patients_route() -> Tuple[Response, int]:
    """
    API endpoint to search patient histories via FTS.
    Accepts a 'q' query parameter.
    e.g., /api/patients/search?q=headache

    :return: JSON response with search results or error message.
    """
    search_term = request.args.get('q', '')
    if not search_term or len(search_term) < 2:
        return jsonify({"message": "Please provide a search term with at least 2 characters."}), 400

    results = search_patient_history(search_term)
    return jsonify(results), 200

def search_encounters_route() -> Tuple[Response, int]:
    """
    API endpoint to search encounters via FTS.
    Accepts a 'q' query parameter.
    e.g., /api/encounters/search?q=headache

    :return: JSON response with search results or error message.
    """
    search_term = request.args.get('q', '')
    if not search_term or len(search_term) < 2:
        return jsonify({"message": "Please provide a search term with at least 2 characters."}), 400
    
    results = search_encounter_history(search_term)
    return jsonify(results), 200


def patient_endpoint_route(patient_id: PatientID) -> Tuple[Response, int]:
    """
    API endpoint to handle patient-related operations.
    :param patient_id: The ID of the patient to operate on, formatted as 'Patient:{patient_id}'.
    :return: Response with patient data or error message.
    """
    logger.debug(f"Patient endpoint called with patient_id: {patient_id}")
    logger.debug(f"Request method: {request.method}")

    if request.method == 'GET':
        # Get a specific patient
        logger.debug(f"Getting patient with ID: {patient_id}")
        patient = get_patient_by_id(patient_id)
        logger.debug(f"Patient result: {patient}")
        if patient:
            return jsonify(patient), 200
        else:
            return jsonify({"error": "Patient not found"}), 404

    elif request.method == 'PUT':
        # Update a patient
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        patient = update_patient(patient_id, data)
        if patient:
            return jsonify(patient), 200
        else:
            return jsonify({"error": "Patient not found or update failed"}), 404

    elif request.method == 'DELETE':
        # Delete a patient
        result = delete_patient(patient_id)
        if result:
            return jsonify({"message": "Patient deleted successfully"}), 200
        else:
            return jsonify({"error": "Patient not found or delete failed"}), 404


def patients_endpoint_route() -> Tuple[Response, int]:
    """
    API endpoint to handle patient-related operations.
    :return: JSON response with patient data or error message.
    """
    if request.method == 'GET':
        # Get all patients
        patients = get_all_patients()
        return jsonify(patients), 200
    elif request.method == 'POST':
        # Create a new patient
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Validate required fields
        required_fields = ['first_name', 'last_name']
        for field in required_fields:
            if not data.get(field):
                return jsonify({"error": f"Missing required field: {field}"}), 400

        patient = create_patient(data)
        if patient:
            return jsonify(patient), 201
        else:
            return jsonify({"error": "Failed to create patient"}), 500


def get_all_encounters_route() -> Tuple[Response, int]:
    """
    API endpoint to get all encounters

    :return: JSON response with all encounters or error message.
    """
    try:
        encounters = get_all_encounters()
        return jsonify(encounters), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def get_encounters_by_patient_route(patient_id: PatientID) -> Tuple[Response, int]:
    """
    API endpoint to get all encounters for a specific patient

    :param patient_id: The ID of the patient to get encounters for, formatted as 'Patient:{patient_id}'.
    :return: JSON response with encounters or error message.
    """
    try:
        encounters = get_encounters_by_patient(patient_id)
        return jsonify(encounters), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def get_encounter_by_id_route(encounter_id: str) -> Tuple[Response, int]:
    """
    API endpoint to get a specific encounter by ID

    :param encounter_id: The ID of the encounter to retrieve.
    :return: JSON response with the encounter or error message.
    """
    try:
        encounter = get_encounter_by_id(encounter_id)
        if encounter:
            return jsonify(encounter), 200
        else:
            return jsonify({"error": "Encounter not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def create_encounter_route(patient_id: PatientID) -> Tuple[Response, int]:
    """
    API endpoint to create a new encounter for a patient

    :param patient_id: The ID of the patient to create an encounter for, formatted as 'Patient:{patient_id}'.
    :return: JSON response with the created encounter or error message.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Validate required fields
        if not data.get("provider_id"):
            return jsonify({"error": "provider_id is required"}), 400
        
        # Set default date if not provided
        if not data.get("date_created"):
            from datetime import datetime
            data["date_created"] = datetime.now().isoformat()
        
        encounter = create_encounter(data, patient_id)
        if encounter:
            return jsonify(encounter), 201
        else:
            return jsonify({"error": "Failed to create encounter"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def update_encounter_route(encounter_id: str) -> Tuple[Response, int]:
    """
    API endpoint to update an encounter

    :param encounter_id: The ID of the encounter to update.
    :return: JSON response with the updated encounter or error message.
    """
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        encounter = update_encounter(encounter_id, data)
        if encounter:
            return jsonify(encounter), 200
        else:
            return jsonify({"error": "Encounter not found or update failed"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def delete_encounter_route(encounter_id: str) -> Tuple[Response, int]:
    """
    API endpoint to delete an encounter

    :param encounter_id: The ID of the encounter to delete.
    :return: JSON response indicating success or failure.
    """
    try:
        success = delete_encounter(encounter_id)
        if success:
            return jsonify({"message": "Encounter deleted successfully"}), 200
        else:
            return jsonify({"error": "Encounter not found or delete failed"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
