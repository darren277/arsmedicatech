"""
CRUD operations for Patient model.
"""
from typing import Any, Dict, List, Union, cast

from lib.db.surreal import AsyncDbController, DbController
from lib.models.patient.common import PatientDict
from lib.models.patient.encounter_crud import add_some_placeholder_encounters
from lib.models.patient.patient_model import Patient
from settings import logger


def store_patient(db: Union[DbController, AsyncDbController], patient: Patient) -> Dict[str, Any]:
    """
    Stores a Patient instance in SurrealDB as patient:<demographic_no>.

    :param db: DbController instance connected to SurrealDB.
    :param patient: Patient instance to store.
    :return: Result of the store operation.
    """
    record_id = f"patient:{patient.demographic_no}"

    content_data: Dict[str, Any] = {
        "demographic_no": str(patient.demographic_no),
        "first_name": patient.first_name,
        "last_name": patient.last_name,
        "date_of_birth": str(patient.date_of_birth),
        "sex": patient.sex,
        "phone": patient.phone,
        "email": patient.email,
        # location could be stored as a separate field or nested object up to you.
        "location": list(patient.location) if patient.location is not None else []
    }

    query = f"CREATE {record_id} CONTENT $data"
    params = {"data": content_data}

    # If the patient record might already exist, consider UPDATE or UPSERT logic instead.
    # For simplicity, we’ll just CREATE each time:
    db.connect()
    result = db.query(query, params)

    logger.debug('resulttttsasfsdgsd', result)

    # If result is a coroutine, await it
    import asyncio
    if asyncio.iscoroutine(result):
        result = asyncio.run(result)

    # If result is a list, return the first item or an empty dict
    if result:
        return result[0]
    elif isinstance(result, dict):
        return result
    else:
        return {}


def add_some_placeholder_patients(db: Union[DbController, AsyncDbController]) -> None:
    """
    Adds some placeholder patients for testing purposes.
    :param db: DbController instance connected to SurrealDB.
    :return: None
    """
    import random
    from datetime import datetime

    # Generate 5 random patients
    for i in range(5):
        demographic_no = random.randint(100, 999)
        first_name = f"FirstName{i+1}"
        last_name = f"LastName{i+1}"
        date_of_birth = datetime.now().replace(year=datetime.now().year - random.randint(20, 60)).isoformat()
        location = (f"City{i+1}", f"State{i+1}", f"Country{i+1}", f"ZipCode{i+1}")
        sex = 'r' if random.choice([True, False]) else 'm'  # Randomly assign 'r' or 'm'
        phone = f"555-01{i+1:02d}{random.randint(1000, 9999)}"
        email = "patient1@gmail.com"

        patient = Patient(
            demographic_no=str(demographic_no),
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            location=location,
            sex=sex,
            phone=phone,
            email=email
        )

        # Store the patient in the database
        store_patient(db, patient)

        add_some_placeholder_encounters(db, f"patient:{demographic_no}")


# TODO: This is still not working 100%.
# Let's write some unit tests to find other edge cases.
def serialize_patient(patient: Any) -> PatientDict:
    """
    Serializes a patient dictionary to ensure all IDs are strings and handles RecordID types.
    :param patient: dict - The patient data to serialize.
    :return: PatientDict - The serialized patient data with all IDs as strings.
    """
    # Handle case where patient is not a dict
    if not isinstance(patient, dict):
        if hasattr(patient, '__str__'):
            return cast(PatientDict, {"demographic_no": str(patient)})
        else:
            return cast(PatientDict, {})
    
    # Create a copy to avoid modifying the original
    result: Dict[str, Any] = {}
    
    # convert patient['id'] to string...
    for key, value in patient.items():
        logger.debug('key', key, value)
        if isinstance(value, list):
            result[key] = [str(item) if isinstance(item, int) else item for item in value]
        elif isinstance(value, int):
            result[key] = str(value)
        else:
            result[key] = value
    return cast(PatientDict, result)


def get_patient_by_id(patient_id: str) -> PatientDict:
    """
    Get a patient by their demographic_no

    :param patient_id: The demographic_no of the patient to retrieve.
    :return: Serialized patient data or empty dict if not found.
    """
    logger.debug(f"Getting patient by ID: {patient_id}")
    db = DbController()
    db.connect()
    
    try:
        # Use a direct query instead of select method
        query = "SELECT * FROM patient WHERE demographic_no = $patient_id"
        params = {"patient_id": patient_id}
        
        logger.debug(f"Executing query: {query} with params: {params}")
        result = db.query(query, params)
        logger.debug(f"Query result: {result}")
        
        # Handle the result structure
        if result and len(result) > 0:
            # Extract the first (and should be only) patient
            patient_data = result[0]
            if 'result' in patient_data:
                patient_data = cast(Dict[str, Any], patient_data['result'][0] if patient_data['result'] else None)
            
            if patient_data:
                serialized_result = serialize_patient(patient_data)
                logger.debug(f"Serialized result: {serialized_result}")
                return serialized_result
            else:
                logger.debug("No patient found in query result")
                return cast(PatientDict, {})
        else:
            logger.debug("No patient found")
            return cast(PatientDict, {})
    except Exception as e:
        logger.debug(f"Error getting patient: {e}")
        return cast(PatientDict, {})
    finally:
        db.close()


def update_patient(patient_id: str, patient_data: Dict[str, Any]) -> PatientDict:
    """
    Update a patient record with only the provided fields, supporting PATCH/partial updates.

    :param patient_id: The demographic_no of the patient to update.
    :param patient_data: A dictionary containing the fields to update.
    :return: Serialized updated patient data or empty dict if not found or no valid fields to update.
    """
    logger.debug(f"Updating patient with ID: {patient_id}")
    db = DbController()
    db.connect()
    
    try:
        # Map 'dob' to 'date_of_birth' if present
        if 'dob' in patient_data:
            patient_data['date_of_birth'] = patient_data.pop('dob')

        # List of valid patient fields
        valid_fields = {
            "first_name", "last_name", "date_of_birth", "sex", "phone", "email", "location",
            "address", "city", "province", "postalCode", "insuranceProvider", "insuranceNumber",
            "medicalConditions", "medications", "allergies", "reasonForVisit", "symptoms",
            "symptomOnset", "consent"
        }

        # Only include fields present in patient_data and valid for the patient
        update_data = {k: v for k, v in patient_data.items() if k in valid_fields and v is not None}

        if not update_data:
            logger.debug("No valid fields to update.")
            return cast(PatientDict, {})

        set_clause = ", ".join([f"{k} = ${k}" for k in update_data.keys()])
        query = f"UPDATE patient SET {set_clause} WHERE demographic_no = $patient_id RETURN *"
        params: Dict[str, Any] = {**update_data, "patient_id": patient_id}

        logger.debug(f"Executing update query: {query} with params: {params}")
        result = db.query(query, params)
        logger.debug(f"Update result: {result}")
        
        # Handle the result structure
        if result and len(result) > 0:
            patient_data = result[0]
            if 'result' in patient_data:
                patient_data = cast(Dict[str, Any], patient_data['result'][0] if patient_data['result'] else None)
            
            if patient_data:
                serialized_result = serialize_patient(patient_data)
                logger.debug(f"Serialized update result: {serialized_result}")
                return serialized_result
            else:
                logger.debug("No patient found in update result")
                return cast(PatientDict, {})
        else:
            logger.debug("Update failed or no patient found")
            return cast(PatientDict, {})
    except Exception as e:
        logger.debug(f"Error updating patient: {e}")
        return cast(PatientDict, {})
    finally:
        db.close()


def delete_patient(patient_id: str) -> bool:
    """
    Delete a patient record

    :param patient_id: The demographic_no of the patient to delete.
    :return: True if the patient was deleted, False if not found or deletion failed, None if an error occurred.
    """
    logger.debug(f"Deleting patient with ID: {patient_id}")
    db = DbController()
    db.connect()
    
    try:
        # Use a direct DELETE query
        query = "DELETE FROM patient WHERE demographic_no = $patient_id"
        params = {"patient_id": patient_id}
        
        logger.debug(f"Executing delete query: {query} with params: {params}")
        result = db.query(query, params)
        logger.debug(f"Delete result: {result}")
        
        # Check if the delete was successful
        if result and len(result) > 0:
            # Check if any records were actually deleted
            delete_info = result[0]
            if 'result' in delete_info:
                deleted_count = len(delete_info['result']) if delete_info['result'] else 0
                logger.debug(f"Deleted {deleted_count} records")
                return deleted_count > 0
            else:
                logger.debug("Delete result structure unexpected")
                return False
        else:
            logger.debug("No delete result")
            return False
    except Exception as e:
        logger.debug(f"Error deleting patient: {e}")
        return False
    finally:
        db.close()


def create_patient(patient_data: Dict[str, Any]) -> PatientDict:
    """
    Create a new patient record

    :param patient_data: A dictionary containing patient information.
    :return: Serialized patient data or empty dict if creation failed.
    """
    logger.debug(f"Creating patient with data: {patient_data}")
    db = DbController()
    db.connect()
    
    try:
        # Generate a new demographic_no if not provided
        if not patient_data.get("demographic_no"):
            logger.debug("No demographic_no provided, generating new one...")
            # Get the highest existing demographic_no and increment
            results = db.select_many('patient')
            if results and len(results) > 0:
                existing_ids = [int(p.get('demographic_no', 0)) for p in results if p.get('demographic_no')]
                new_id = max(existing_ids) + 1 if existing_ids else 1000
            else:
                new_id = 1000
            patient_data["demographic_no"] = str(new_id)
            logger.debug(f"Generated demographic_no: {new_id}")
        
        # Create Patient object
        loc = patient_data.get("location", [])

        patient = Patient(
            demographic_no=patient_data["demographic_no"],
            first_name=patient_data.get("first_name"),
            last_name=patient_data.get("last_name"),
            date_of_birth=patient_data.get("date_of_birth"),
            location=tuple(loc),
            sex=patient_data.get("sex"),
            phone=patient_data.get("phone"),
            email=patient_data.get("email")
        )
        
        logger.debug(f"Created Patient object: {patient}")
        result = store_patient(db, patient)
        logger.debug(f"Store patient result: {result}")
        
        # Handle different result structures
        if result and isinstance(result, list) and len(result) > 0:
            first_result = result[0]
            if isinstance(first_result, dict) and 'result' in first_result:
                final_result = serialize_patient(first_result['result'])
            else:
                final_result = serialize_patient(first_result)
        elif result and isinstance(result, dict):
            final_result = serialize_patient(result)
        else:
            final_result = cast(PatientDict, {})
        
        logger.debug(f"Final patient result: {final_result}")
        return final_result
    except Exception as e:
        logger.debug(f"Error creating patient: {e}")
        return cast(PatientDict, {})
    finally:
        db.close()


# TODO: Implement pagination.

def get_all_patients() -> List[PatientDict]:
    """
    Get all patients from the database

    :return: List of serialized Patient objects or an empty list if no patients found.
    """
    db = DbController()
    db.connect()
    
    try:
        logger.debug("Getting all patients from database...")
        results = db.select_many('patient')
        logger.debug(f"Raw results: {results}")
        
        # Handle different result structures
        if results and len(results) > 0:
            # If the first result has a 'result' key, extract the actual data
            if 'result' in results[0]:
                patients = results[0]['result']
            else:
                patients = results
            
            logger.debug(f"Processed patients: {patients}")
            
            if isinstance(patients, list):
                serialized_patients = [serialize_patient(patient) for patient in patients]
                logger.debug(f"Serialized patients: {serialized_patients}")
                return serialized_patients
            else:
                logger.debug("Patients is not a list")
                return []
        else:
            logger.debug("No results or empty results")
            return []
    except Exception as e:
        logger.debug(f"Error getting all patients: {e}")
        return []
    finally:
        db.close()
