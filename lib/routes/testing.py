""""""
from flask import jsonify, session, request

from lib.db.surreal import DbController
from lib.models.patient import add_some_placeholder_patients, create_patient, get_patient_by_id, update_patient, \
    delete_patient
from settings import logger


def test_surrealdb_route():
    db = DbController()
    db.connect()

    # create_schema()

    add_some_placeholder_patients(db)

    results = db.select_many('patient')
    logger.info("RESULTS: " + str(results))
    return jsonify({"message": "Test completed."})


def test_crud_route():
    try:
        # Test creating a patient
        test_patient_data = {
            "first_name": "Test",
            "last_name": "Patient",
            "date_of_birth": "1990-01-01",
            "sex": "M",
            "phone": "555-1234",
            "email": "test@example.com",
            "location": ["Test City", "Test State", "Test Country", "12345"]
        }

        created_patient = create_patient(test_patient_data)
        if not created_patient:
            return jsonify({"error": "Failed to create patient"}), 500

        patient_id = created_patient.get('demographic_no')

        # Test reading the patient
        read_patient = get_patient_by_id(patient_id)
        if not read_patient:
            return jsonify({"error": "Failed to read patient"}), 500

        # Test updating the patient
        update_data = {"phone": "555-5678"}
        updated_patient = update_patient(patient_id, update_data)
        if not updated_patient:
            return jsonify({"error": "Failed to update patient"}), 500

        # Test deleting the patient
        delete_result = delete_patient(patient_id)
        if not delete_result:
            return jsonify({"error": "Failed to delete patient"}), 500

        return jsonify({
            "message": "CRUD operations test completed successfully",
            "created": created_patient,
            "read": read_patient,
            "updated": updated_patient,
            "deleted": delete_result
        })

    except Exception as e:
        logger.error(f"CRUD test failed: {e}")
        return jsonify({"error": f"CRUD test failed: {str(e)}"}), 500

def debug_session_route():
    """Debug endpoint to check session state"""
    logger.debug(f"Session data: {dict(session)}")
    logger.debug(f"Request headers: {dict(request.headers)}")
    return jsonify({
        "session": dict(session),
        "headers": dict(request.headers)
    })
