""""""
from flask import request, jsonify

from lib.models.patient import update_patient, search_patient_history, get_patient_by_id, delete_patient, \
    get_all_patients, create_patient, get_all_encounters, get_encounters_by_patient, get_encounter_by_id, \
    create_encounter, update_encounter, delete_encounter, search_encounter_history
from settings import logger


def patch_intake_route(patient_id):
    payload = request.get_json()
    print(f"[DEBUG] Patching patient {patient_id} with payload: {payload}")

    # Map 'User:' to patient ID if needed
    patient_id = patient_id.replace('User:', '')

    result = update_patient(patient_id, payload)
    print(f"[DEBUG] Update result: {result}")
    if not result:
        logger.error(f"Failed to update patient {patient_id}: {result}")
        return jsonify({"error": "Failed to update patient"}), 400
    return jsonify({'ok': True}), 200


def search_patients_route():
    """
        API endpoint to search patient histories via FTS.
        Accepts a 'q' query parameter.
        e.g., /api/patients/search?q=headache
        """
    search_term = request.args.get('q', '')
    if not search_term or len(search_term) < 2:
        return jsonify({"message": "Please provide a search term with at least 2 characters."}), 400

    results = search_patient_history(search_term)
    return jsonify(results)

def search_encounters_route():
    """
    API endpoint to search encounters via FTS.
    Accepts a 'q' query parameter.
    e.g., /api/encounters/search?q=headache
    """
    search_term = request.args.get('q', '')
    if not search_term or len(search_term) < 2:
        return jsonify({"message": "Please provide a search term with at least 2 characters."}), 400
    
    results = search_encounter_history(search_term)
    return jsonify(results)


def patient_endpoint_route(patient_id):
    print(f"[DEBUG] Patient endpoint called with patient_id: {patient_id}")
    print(f"[DEBUG] Request method: {request.method}")

    if request.method == 'GET':
        # Get a specific patient
        print(f"[DEBUG] Getting patient with ID: {patient_id}")
        patient = get_patient_by_id(patient_id)
        print(f"[DEBUG] Patient result: {patient}")
        if patient:
            return jsonify(patient)
        else:
            return jsonify({"error": "Patient not found"}), 404

    elif request.method == 'PUT':
        # Update a patient
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        patient = update_patient(patient_id, data)
        if patient:
            return jsonify(patient)
        else:
            return jsonify({"error": "Patient not found or update failed"}), 404

    elif request.method == 'DELETE':
        # Delete a patient
        result = delete_patient(patient_id)
        if result:
            return jsonify({"message": "Patient deleted successfully"})
        else:
            return jsonify({"error": "Patient not found or delete failed"}), 404


def patients_endpoint_route():
    if request.method == 'GET':
        # Get all patients
        patients = get_all_patients()
        return jsonify(patients)
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


def get_all_encounters_route():
    """API endpoint to get all encounters"""
    try:
        encounters = get_all_encounters()
        return jsonify(encounters)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def get_encounters_by_patient_route(patient_id):
    """API endpoint to get all encounters for a specific patient"""
    try:
        encounters = get_encounters_by_patient(patient_id)
        return jsonify(encounters)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def get_encounter_by_id_route(encounter_id):
    """API endpoint to get a specific encounter by ID"""
    try:
        encounter = get_encounter_by_id(encounter_id)
        if encounter:
            return jsonify(encounter)
        else:
            return jsonify({"error": "Encounter not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def create_encounter_route(patient_id):
    """API endpoint to create a new encounter for a patient"""
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


def update_encounter_route(encounter_id):
    """API endpoint to update an encounter"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        encounter = update_encounter(encounter_id, data)
        if encounter:
            return jsonify(encounter)
        else:
            return jsonify({"error": "Encounter not found or update failed"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def delete_encounter_route(encounter_id):
    """API endpoint to delete an encounter"""
    try:
        success = delete_encounter(encounter_id)
        if success:
            return jsonify({"message": "Encounter deleted successfully"})
        else:
            return jsonify({"error": "Encounter not found or delete failed"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
