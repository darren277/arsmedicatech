"""
Patient and Encounter Models for SurrealDB
"""
from typing import Any, Dict, List, Optional, Tuple, Union, cast

from surrealdb import RecordID

from lib.db.surreal import AsyncDbController, DbController
from settings import logger

PatientDict = Dict[str, str | int | List[Any] | None]  # Define a type for patient dictionaries

EncounterDict = Dict[str, str | int | List[Any] | None]  # Define a type for encounter dictionaries


class Patient:
    """
    Represents a patient in the system.
    """
    def __init__(
            self,
            demographic_no: str,
            first_name: Optional[str] = None,
            last_name: Optional[str] = None,
            date_of_birth: Optional[str] = None,
            location: Optional[Tuple[str, str, str, str]] = None,
            sex: Optional[str] = None,
            phone: Optional[str] = None,
            email: Optional[str] = None
    ) -> None:
        """
        Initializes a Patient instance.
        :param demographic_no: Unique identifier for the patient.
        :param first_name: Patient's first name.
        :param last_name: Patient's last name.
        :param date_of_birth: Patient's date of birth in ISO format (YYYY-MM-DD).
        :param location: Tuple containing (city, province, country, postal code).
        :param sex: Patient's sex
        :param phone: Patient's phone number.
        :param email: Patient's email address.
        """
        self.demographic_no = demographic_no
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.location = location
        self.sex = sex
        self.phone = phone
        self.email = email
        self.address = None

        self.alerts: List[Any] = []
        self.ext_attributes: Dict[str, Any] = {}      # For demographicExt key-value pairs
        self.encounters: List[Any] = []          # List of Encounter objects
        self.cpp_issues: List[Any] = []          # Summaries from casemgmt_cpp or casemgmt_issue
        self.ticklers: List[Any] = []           # Tickler (reminders/follow-up tasks)

    def __repr__(self) -> str:
        return f"<Patient: {self.first_name} {self.last_name} (ID: {self.demographic_no})>"

    def schema(self) -> List[str]:
        """
        Defines the schema for the Patient table in SurrealDB.
        :return: list of schema definition statements.
        """
        statements: List[str] = []
        statements.append('DEFINE TABLE patient SCHEMAFULL;')
        statements.append('DEFINE FIELD demographic_no ON patient TYPE string ASSERT $value != none;')
        statements.append('DEFINE FIELD first_name ON patient TYPE string;')
        statements.append('DEFINE FIELD last_name ON patient TYPE string;')
        statements.append('DEFINE FIELD date_of_birth ON patient TYPE string;')
        statements.append('DEFINE FIELD sex ON patient TYPE string;')
        statements.append('DEFINE FIELD phone ON patient TYPE string;')
        statements.append('DEFINE FIELD email ON patient TYPE string;')
        statements.append('DEFINE FIELD location ON patient TYPE array;')

        statements.append('DEFINE INDEX idx_patient_demographic_no ON patient FIELDS demographic_no UNIQUE;')

        return statements



class SOAPNotes:
    """
    Represents SOAP notes for an encounter.
    """
    def __init__(self, subjective: str, objective: str, assessment: str, plan: str) -> None:
        """
        Initializes a SOAPNotes instance.
        :param subjective: Subjective observations from the patient.
        :param objective: Objective findings from the examination.
        :param assessment: Assessment of the patient's condition.
        :param plan: Plan for treatment or follow-up.
        :return: None
        """
        self.subjective = subjective
        self.objective = objective
        self.assessment = assessment
        self.plan = plan

    def serialize(self) -> Dict[str, Any]:
        """
        Serializes the SOAPNotes instance to a dictionary.
        :return: dict containing the SOAP notes.
        """
        return dict(
            subjective=self.subjective,
            objective=self.objective,
            assessment=self.assessment,
            plan=self.plan
        )

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'SOAPNotes':
        """
        Creates a SOAPNotes instance from a dictionary.
        :param data: dict containing SOAP notes fields.
        :return: SOAPNotes instance
        """
        return cls(
            subjective=str(data.get('subjective') or ""),
            objective=str(data.get('objective') or ""),
            assessment=str(data.get('assessment') or ""),
            plan=str(data.get('plan') or "")
        )


class Encounter:
    """
    Represents an encounter note in the system.
    """
    def __init__(
            self,
            note_id: str,
            date_created: str,
            provider_id: str,
            soap_notes: Optional[SOAPNotes] = None,
            additional_notes: Optional[str] = None,
            diagnostic_codes: Optional[List[str]] = None
    ) -> None:
        """
        Initializes an Encounter instance.
        :param note_id: Unique identifier for the encounter note.
        :param date_created: Date when the encounter note was created (ISO format).
        :param provider_id: Unique identifier for the healthcare provider.
        :param soap_notes: SOAPNotes object containing the structured notes.
        :param additional_notes: Additional notes or comments for the encounter.
        :param diagnostic_codes: List of diagnostic codes associated with the encounter.
        :return: None
        """
        self.note_id = note_id
        self.date_created = date_created
        self.provider_id = provider_id
        self.soap_notes = soap_notes
        self.additional_notes = additional_notes
        self.diagnostic_codes = diagnostic_codes
        self.status = None  # e.g., locked, signed, etc.

    def __repr__(self) -> str:
        return f"<Encounter note_id={self.note_id}, date={self.date_created}>"

    def schema(self) -> List[str]:
        """
        Defines the schema for the Encounter table in SurrealDB.
        :return: list of schema definition statements.
        """
        statements: List[str] = []

        # Define a standard analyzer for medical text.
        # It splits text into words and converts them to a common format (lowercase, basic characters).
        statements.append("""
            DEFINE ANALYZER medical_text_analyzer 
            TOKENIZERS class 
            FILTERS lowercase, ascii;
        """)

        statements.append('DEFINE TABLE encounter SCHEMAFULL;')
        statements.append('DEFINE FIELD note_id ON encounter TYPE string ASSERT $value != none;')
        statements.append('DEFINE FIELD date_created ON encounter TYPE string;')
        statements.append('DEFINE FIELD provider_id ON encounter TYPE string;')
        statements.append('DEFINE FIELD note_text ON encounter TYPE string;')
        statements.append('DEFINE FIELD diagnostic_codes ON encounter TYPE array;')

        statements.append('DEFINE FIELD patient ON encounter TYPE record<patient> ASSERT $value != none;')

        # This index is specifically for full-text search on the 'note_text' field.
        # It uses our custom analyzer and enables relevance scoring (BM25) and highlighting.
        statements.append("""
            DEFINE INDEX idx_encounter_notes ON TABLE encounter 
            FIELDS note_text 
            SEARCH ANALYZER medical_text_analyzer BM25 HIGHLIGHTS;
        """)

        statements.append('DEFINE INDEX idx_encounter_note_id ON encounter FIELDS note_id UNIQUE;')

        return statements


def create_schema() -> None:
    """
    Creates the schema for Patient and Encounter tables in SurrealDB.
    :return: None
    """
    db = DbController(namespace='arsmedicatech', database='patients')
    db.connect()

    patient = Patient("")
    encounter = Encounter("", "", "")

    for stmt in patient.schema():
        db.query(stmt)

    for stmt in encounter.schema():
        db.query(stmt)

    db.close()


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

def store_encounter(db: Union[DbController, AsyncDbController], encounter: Encounter, patient_id: str) -> Dict[str, Any]:
    """
    Stores an Encounter instance in SurrealDB as encounter:<note_id>,
    referencing the given patient_id (e.g., 'patient:12345').

    :param db: DbController instance connected to SurrealDB.
    :param encounter: Encounter instance to store.
    :param patient_id: Patient ID in the format 'patient:<demographic_no>'.
    :return: Result of the store operation.
    """
    record_id = f"encounter:{encounter.note_id}"

    note_text: str = ""

    # Handle note_text properly - check if soap_notes is a SOAPNotes object or a string
    if encounter.soap_notes and hasattr(encounter.soap_notes, 'serialize'):
        note_text = str(encounter.soap_notes.serialize())
    else:
        if encounter.soap_notes:
            note_text = str(encounter.soap_notes.serialize())
        else:
            note_text = encounter.additional_notes or ""

    content_data: Dict[str, Any] = {
        "note_id": str(encounter.note_id),
        "date_created": str(encounter.date_created),
        "provider_id": str(encounter.provider_id),
        "note_text": note_text,
        "diagnostic_codes": encounter.diagnostic_codes
    }

    query = f"CREATE {record_id}\n"
    set_query = f"""SET  note_id = $note_id,
                        date_created = $date_created,
                        provider_id = $provider_id,
                        note_text = $note_text,
                        diagnostic_codes = $diagnostic_codes,
                        patient = {patient_id}
    """

    params = content_data
    db.connect()
    query += set_query
    result = db.query(query, params)

    logger.debug('resultttt', result)

    # If result is a coroutine, await it
    import asyncio
    if asyncio.iscoroutine(result):
        result = asyncio.run(result)

    # If result is a list, return the first item or an empty dict
    if result:
        return result[0] if len(result) > 0 else {}
    elif isinstance(result, dict):
        return result
    else:
        return {}


def add_some_placeholder_encounters(db: Union[DbController, AsyncDbController], patient_id: str) -> None:
    """
    Adds some placeholder encounters for testing purposes.

    :param db: DbController instance connected to SurrealDB.
    :param patient_id: Patient ID in the format 'patient:<demographic_no>'.
    :return: None
    """
    import random
    from datetime import datetime, timedelta

    # Generate 5 random encounters
    for i in range(5):
        note_id = random.randint(100, 999)
        date_created = datetime.now() - timedelta(days=random.randint(1, 30))
        provider_id = f"provider-{random.randint(1, 10)}"
        note_text = f"This is a placeholder note text for encounter {i+1}."
        diagnostic_codes = [f"code-{random.randint(100, 999)}"]

        encounter = Encounter(str(note_id), date_created.isoformat(), provider_id, additional_notes=note_text, diagnostic_codes=diagnostic_codes)
        store_encounter(db, encounter, patient_id)


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

def serialize_encounter(encounter: Any) -> EncounterDict:
    """
    Serializes an encounter dictionary to ensure all IDs are strings and handles RecordID types.
    :param encounter: dict - The encounter data to serialize.
    :return: EncounterDict - The serialized encounter data with all IDs as strings.
    """
    # Handle case where encounter is not a dict
    if not isinstance(encounter, dict):
        if hasattr(encounter, '__str__'):
            return cast(EncounterDict, {"id": str(encounter.id), "note_id": str(encounter.note_id), "patient": str(encounter.patient)})
        else:
            return cast(EncounterDict, {})
    
    # Create a copy to avoid modifying the original
    result: Dict[str, Any] = {}
    
    # convert encounter['id'] to string...
    for key, value in encounter.items():
        logger.debug('key [encounter]', key, value)
        if isinstance(value, list):
            result[key] = [str(item) if isinstance(item, int) else item for item in value]
        elif isinstance(value, int):
            result[key] = str(value)
        elif key == 'patient' and isinstance(value, dict):
            result[key] = serialize_patient(value)
        elif key == 'patient' and isinstance(value, RecordID):
            result[key] = str(value)
        elif key == 'id' and isinstance(value, RecordID):
            result[key] = str(value)
        else:
            result[key] = value
    return cast(EncounterDict, result)

def search_patient_history(search_term: str) -> List[PatientDict]:
    """
    Performs a full-text search across all encounter notes.

    :param search_term: The term to search for in the encounter notes.
    :return: List of Encounter objects that match the search term.
    """
    db = DbController()
    db.connect()

    logger.debug("ATTEMPTING SEARCH", search_term)

    # This query searches the 'note_text' field.
    # @0@ is a predicate that links to search::score(0) and search::highlight(0).
    # We fetch the score, the highlighted note text, and the associated patient record.
    query = """
        SELECT
            search::score(0) AS score,
            search::highlight('<b>', '</b>', 0) AS highlighted_note,
            patient.*,
            *
        FROM encounter
        WHERE note_text @0@ $query
        ORDER BY score DESC
        LIMIT 15;
    """
    params = {"query": search_term}

    try:
        results = db.query(query, params)
        # Assuming the first result list from the multi-statement response is what we need.
        if results and len(results) > 0:
            logger.debug("SEARCH RESULTS", results)
            serialized_results: List[PatientDict] = []
            for e in results:
                result = serialize_encounter(e)
                serialized_results.append(result)
            return serialized_results
        return []
    except Exception as e:
        logger.error(f"Error during search: {e}")
        return []
    finally:
        db.close()

def search_encounter_history(search_term: str) -> List[EncounterDict]:
    """
    Performs a full-text search across all encounter notes.

    :param search_term: The term to search for in the encounter notes.
    :return: List of Encounter objects that match the search term.
    """
    db = DbController()
    db.connect()
    
    logger.debug("ATTEMPTING SEARCH", search_term)
    
    query = """
        SELECT
            search::score(0) AS score,
            search::highlight('<b>', '</b>', 0) AS highlighted_note,
            patient.*,
            *
        FROM encounter
        WHERE note_text @0@ $query
        ORDER BY score DESC
        LIMIT 15;
    """
    params = {"query": search_term}

    try:
        results = db.query(query, params)
        if results and len(results) > 0:
            logger.debug("SEARCH RESULTS", results)
            serialized_results: List[EncounterDict] = []
            for e in results:
                result = serialize_encounter(e)
                serialized_results.append(result)
            return serialized_results
        return []
    except Exception as e:
        logger.error(f"Error during search: {e}")
        return []
    finally:
        db.close()


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


def get_all_encounters() -> List[EncounterDict]:
    """
    Get all encounters from the database

    :return: List of serialized Encounter objects or an empty list if no encounters found.
    """
    db = DbController()
    db.connect()
    
    try:
        logger.debug("Getting all encounters from database...")
        results = db.select_many('encounter')
        logger.debug(f"Raw encounter results: {results}")
        
        # Handle different result structures
        if results and len(results) > 0:
            # If the first result has a 'result' key, extract the actual data
            if 'result' in results[0]:
                encounters = results[0]['result']
            else:
                encounters = results
            
            logger.debug(f"Processed encounters: {encounters}")
            
            if isinstance(encounters, list):
                serialized_encounters = [serialize_encounter(encounter) for encounter in encounters]
                logger.debug(f"Serialized encounters: {serialized_encounters}")
                return serialized_encounters
            else:
                logger.debug("Encounters is not a list")
                return []
        else:
            logger.debug("No encounter results or empty results")
            return []
    except Exception as e:
        logger.debug(f"Error getting all encounters: {e}")
        return []
    finally:
        db.close()


def get_encounter_by_id(encounter_id: str) -> EncounterDict:
    """
    Get an encounter by its note_id

    :param encounter_id: The note_id of the encounter to retrieve.
    :return: Serialized encounter data or empty dict if not found.
    """
    logger.debug(f"Getting encounter by ID: {encounter_id}")
    db = DbController()
    db.connect()
    
    try:
        query = "SELECT * FROM encounter WHERE note_id = $encounter_id"
        params = {"encounter_id": encounter_id}
        
        logger.debug(f"Executing encounter query: {query} with params: {params}")
        result = db.query(query, params)
        logger.debug(f"Encounter query result: {result}")
        
        # Handle the result structure
        if result and isinstance(result, list) and len(result) > 0:
            encounter_data = result[0]
            if isinstance(encounter_data, dict) and 'result' in encounter_data:
                encounter_data = cast(Dict[str, Any], encounter_data['result'][0] if encounter_data['result'] else None)
            
            if encounter_data:
                serialized_result = serialize_encounter(encounter_data)
                logger.debug(f"Serialized encounter result: {serialized_result}")
                return serialized_result
            else:
                logger.debug("No encounter found in query result")
                return cast(EncounterDict, {})
        else:
            logger.debug("No encounter found")
            return cast(EncounterDict, {})
    except Exception as e:
        logger.debug(f"Error getting encounter: {e}")
        return cast(EncounterDict, {})
    finally:
        db.close()


def get_encounters_by_patient(patient_id: str) -> List[EncounterDict]:
    """
    Get all encounters for a specific patient

    :param patient_id: The demographic_no of the patient to retrieve encounters for.
    :return: List of serialized Encounter objects or an empty list if no encounters found.
    """
    logger.debug(f"Getting encounters for patient: {patient_id}")
    db = DbController()
    db.connect()
    
    try:
        query = "SELECT * FROM encounter WHERE patient = $patient_id ORDER BY date_created DESC"
        params = {"patient_id": f"patient:{patient_id}"}
        
        logger.debug(f"Executing patient encounters query: {query} with params: {params}")
        result = db.query(query, params)
        logger.debug(f"Patient encounters query result: {result}")
        
        # Handle the result structure
        if result and len(result) > 0:
            encounters_data = result[0]
            if 'result' in encounters_data:
                encounters = encounters_data['result']
            else:
                encounters = result
            
            if isinstance(encounters, list):
                serialized_encounters = [serialize_encounter(encounter) for encounter in encounters]
                logger.debug(f"Serialized patient encounters: {serialized_encounters}")
                return serialized_encounters
            else:
                logger.debug("Patient encounters is not a list")
                return []
        else:
            logger.debug("No patient encounters found")
            return []
    except Exception as e:
        logger.debug(f"Error getting patient encounters: {e}")
        return []
    finally:
        db.close()


def create_encounter(encounter_data: Dict[str, Any], patient_id: str) -> EncounterDict:
    """
    Create a new encounter record

    :param encounter_data: A dictionary containing encounter information.
    :param patient_id: The demographic_no of the patient to associate with the encounter.
    :return: Serialized encounter data or empty dict if creation failed.
    """
    logger.debug(f"Creating encounter with data: {encounter_data}")
    db = DbController()
    db.connect()
    
    try:
        # Generate a new note_id if not provided
        if not encounter_data.get("note_id"):
            logger.debug("No note_id provided, generating new one...")
            results = db.select_many('encounter')
            if results and len(results) > 0:
                existing_ids = [int(e.get('note_id', 0)) for e in results if e.get('note_id')]
                new_id = max(existing_ids) + 1 if existing_ids else 1000
            else:
                new_id = 1000
            encounter_data["note_id"] = str(new_id)
            logger.debug(f"Generated note_id: {new_id}")
        
        # Create Encounter object
        encounter = Encounter(
            note_id=encounter_data["note_id"],
            date_created=str(encounter_data.get("date_created") or ""),
            provider_id=str(encounter_data.get("provider_id") or ""),
            additional_notes=str(encounter_data.get("note_text") or ""),
            diagnostic_codes=encounter_data.get("diagnostic_codes", [])
        )
        
        logger.debug(f"Created Encounter object: {encounter}")
        result = store_encounter(db, encounter, f"patient:{patient_id}")
        logger.debug(f"Store encounter result: {result}")
        
        # Handle different result structures
        if result and isinstance(result, list) and len(result) > 0:
            first_result = result[0]
            if isinstance(first_result, dict) and 'result' in first_result:
                final_result = serialize_encounter(first_result['result'])
            else:
                final_result = serialize_encounter(first_result)
        elif result:
            final_result = serialize_encounter(result)
        else:
            final_result = cast(EncounterDict, {})
        
        logger.debug(f"Final encounter result: {final_result}")
        return final_result
    except Exception as e:
        logger.debug(f"Error creating encounter: {e}")
        return cast(EncounterDict, {})
    finally:
        db.close()


def update_encounter(encounter_id: str, encounter_data: Dict[str, Any]) -> EncounterDict:
    """
    Update an encounter record with only the provided fields

    :param encounter_id: The note_id of the encounter to update.
    :param encounter_data: A dictionary containing the fields to update.
    :return: Serialized updated encounter data or empty dict if not found or no valid fields to update.
    """
    logger.debug(f"Updating encounter with ID: {encounter_id}")
    db = DbController()
    db.connect()
    
    try:
        # List of valid encounter fields
        valid_fields = {
            "date_created", "provider_id", "note_text", "diagnostic_codes", "status"
        }

        # Only include fields present in encounter_data and valid for the encounter
        update_data = {k: v for k, v in encounter_data.items() if k in valid_fields and v is not None}

        if not update_data:
            logger.debug("No valid fields to update for encounter.")
            return cast(EncounterDict, {})

        set_clause = ", ".join([f"{k} = ${k}" for k in update_data.keys()])
        query = f"UPDATE encounter SET {set_clause} WHERE note_id = $encounter_id RETURN *"
        params: Dict[str, Any] = {**update_data, "encounter_id": encounter_id}

        logger.debug(f"Executing encounter update query: {query} with params: {params}")
        result = db.query(query, params)
        logger.debug(f"Encounter update result: {result}")
        
        # Handle the result structure
        if result and len(result) > 0:
            encounter_data = result[0]
            if 'result' in encounter_data:
                encounter_data = cast(Dict[str, Any], encounter_data['result'][0] if encounter_data['result'] else None)
            
            if encounter_data:
                serialized_result = serialize_encounter(encounter_data)
                logger.debug(f"Serialized encounter update result: {serialized_result}")
                return serialized_result
            else:
                logger.debug("No encounter found in update result")
                return cast(EncounterDict, {})
        else:
            logger.debug("Encounter update failed or no encounter found")
            return cast(EncounterDict, {})
    except Exception as e:
        logger.debug(f"Error updating encounter: {e}")
        return cast(EncounterDict, {})
    finally:
        db.close()


def delete_encounter(encounter_id: str) -> bool:
    """
    Delete an encounter record

    :param encounter_id: The note_id of the encounter to delete.
    :return: True if the encounter was deleted, False if not found or deletion failed, None if an error occurred.
    """
    logger.debug(f"Deleting encounter with ID: {encounter_id}")
    db = DbController()
    db.connect()
    
    try:
        query = "DELETE FROM encounter WHERE note_id = $encounter_id"
        params = {"encounter_id": encounter_id}
        
        logger.debug(f"Executing encounter delete query: {query} with params: {params}")
        result = db.query(query, params)
        logger.debug(f"Encounter delete result: {result}")
        
        # Check if the delete was successful
        if result and len(result) > 0:
            delete_info = result[0]
            if 'result' in delete_info:
                deleted_count = len(delete_info['result']) if delete_info['result'] else 0
                logger.debug(f"Deleted {deleted_count} encounter records")
                return deleted_count > 0
            else:
                logger.debug("Encounter delete result structure unexpected")
                return False
        else:
            logger.debug("No encounter delete result")
            return False
    except Exception as e:
        logger.debug(f"Error deleting encounter: {e}")
        return False
    finally:
        db.close()


#create_schema()
