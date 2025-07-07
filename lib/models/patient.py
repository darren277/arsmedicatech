""""""
from typing import Tuple

from lib.db.surreal import DbController


class Patient:
    def __init__(self, demographic_no, first_name: str = None, last_name: str  = None, date_of_birth: str = None,
                 location: Tuple[str, str, str, str] = None, sex: chr = None, phone: str = None, email: str = None):
        self.demographic_no = demographic_no
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.location = location
        self.sex = sex
        self.phone = phone
        self.email = email
        self.address = None

        self.alerts = []
        self.ext_attributes = {}      # For demographicExt key-value pairs
        self.encounters = []          # List of Encounter objects
        self.cpp_issues = []          # Summaries from casemgmt_cpp or casemgmt_issue
        self.ticklers = []           # Tickler (reminders/follow-up tasks)

    def __repr__(self):
        return f"<Patient: {self.first_name} {self.last_name} (ID: {self.demographic_no})>"

    def schema(self):
        statements = []
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



class Encounter:
    def __init__(self, note_id, date_created, provider_id, note_text=None, diagnostic_codes=None):
        self.note_id = note_id
        self.date_created = date_created
        self.provider_id = provider_id
        self.note_text = note_text
        self.diagnostic_codes = diagnostic_codes
        self.status = None  # e.g., locked, signed, etc.

    def __repr__(self):
        return f"<Encounter note_id={self.note_id}, date={self.date_created}>"

    def schema(self):
        statements = []

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


def create_schema():
    db = DbController(namespace='arsmedicatech', database='patients')
    db.connect()

    patient = Patient(None)
    encounter = Encounter(None, None, None)

    for stmt in patient.schema():
        db.query(stmt)

    for stmt in encounter.schema():
        db.query(stmt)

    db.close()


def store_patient(db, patient: Patient):
    """
    Stores a Patient instance in SurrealDB as patient:<demographic_no>.
    """
    record_id = f"patient:{patient.demographic_no}"

    content_data = {
        "demographic_no": str(patient.demographic_no),
        "first_name": patient.first_name,
        "last_name": patient.last_name,
        "date_of_birth": str(patient.date_of_birth),
        "sex": patient.sex,
        "phone": patient.phone,
        "email": patient.email,
        # location could be stored as a separate field or nested object up to you.
        "location": list(patient.location)
    }

    query = f"CREATE {record_id} CONTENT $data"
    params = {"data": content_data}

    # If the patient record might already exist, consider UPDATE or UPSERT logic instead.
    # For simplicity, we’ll just CREATE each time:
    db.connect()
    result = db.query(query, params)

    print('resulttttsasfsdgsd', result)

    return result

def store_encounter(db, encounter: Encounter, patient_id: str):
    """
    Stores an Encounter instance in SurrealDB as encounter:<note_id>,
    referencing the given patient_id (e.g., 'patient:12345').
    """
    record_id = f"encounter:{encounter.note_id}"

    content_data = {
        "note_id": str(encounter.note_id),
        "date_created": str(encounter.date_created),
        "provider_id": str(encounter.provider_id),
        "note_text": encounter.note_text,
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

    print('resultttt', result)

    return result


def add_some_placeholder_encounters(db, patient_id: str):
    """
    Adds some placeholder encounters for testing purposes.
    """
    from datetime import datetime, timedelta
    import random

    # Generate 5 random encounters
    for i in range(5):
        note_id = random.randint(100, 999)
        date_created = datetime.now() - timedelta(days=random.randint(1, 30))
        provider_id = f"provider-{random.randint(1, 10)}"
        note_text = f"This is a placeholder note text for encounter {i+1}."
        diagnostic_codes = [f"code-{random.randint(100, 999)}"]

        encounter = Encounter(note_id, date_created.isoformat(), provider_id, note_text, diagnostic_codes)
        store_encounter(db, encounter, patient_id)


def add_some_placeholder_patients(db):
    """
    Adds some placeholder patients for testing purposes.
    :param db:
    :return:
    """
    from datetime import datetime
    import random

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
            demographic_no=demographic_no,
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


def serialize_patient(patient):
    from surrealdb import RecordID
    # convert patient['id'] to string...
    for key in patient:
        print('key', key, patient[key])
        if type(patient[key]) == RecordID:
            patient[key] = str(patient[key])
        elif isinstance(patient[key], list):
            patient[key] = [str(item) if isinstance(item, int) else item for item in patient[key]]
        elif isinstance(patient[key], int):
            patient[key] = str(patient[key])
    return patient

def serialize_encounter(encounter):
    from surrealdb import RecordID
    # convert patient['id'] to string...
    for key in encounter:
        print('key [encounter]', key, encounter[key])
        if type(encounter[key]) == RecordID:
            encounter[key] = str(encounter[key])
        elif isinstance(encounter[key], list):
            encounter[key] = [str(item) if isinstance(item, int) else item for item in encounter[key]]
        elif isinstance(encounter[key], int):
            encounter[key] = str(encounter[key])
        if 'patient' in encounter:
            encounter['patient'] = serialize_patient(encounter['patient'])
    return encounter

def search_patient_history(search_term: str):
    """Performs a full-text search across all encounter notes."""
    db = DbController()
    db.connect()

    print("ATTEMPTING SEARCH", search_term)

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
        if results and isinstance(results, list) and len(results) > 0:
            print("SEARCH RESULTS", results)
            return [serialize_encounter(e) for e in results]
        return []
    except Exception as e:
        logger.error(f"Error during search: {e}")
        return []
    finally:
        db.close()


def get_patient_by_id(patient_id: str):
    """Get a patient by their demographic_no"""
    db = DbController()
    db.connect()
    
    try:
        record_id = f"patient:{patient_id}"
        result = db.select(record_id)
        
        if result:
            return serialize_patient(result)
        return None
    except Exception as e:
        print(f"Error getting patient: {e}")
        return None
    finally:
        db.close()


def update_patient(patient_id: str, patient_data: dict):
    """Update a patient record"""
    db = DbController()
    db.connect()
    
    try:
        record_id = f"patient:{patient_id}"
        
        # Prepare the data for update
        update_data = {
            "first_name": patient_data.get("first_name"),
            "last_name": patient_data.get("last_name"),
            "date_of_birth": patient_data.get("date_of_birth"),
            "sex": patient_data.get("sex"),
            "phone": patient_data.get("phone"),
            "email": patient_data.get("email"),
            "location": patient_data.get("location", [])
        }
        
        # Remove None values
        update_data = {k: v for k, v in update_data.items() if v is not None}
        
        result = db.update(record_id, update_data)
        
        if result:
            return serialize_patient(result)
        return None
    except Exception as e:
        print(f"Error updating patient: {e}")
        return None
    finally:
        db.close()


def delete_patient(patient_id: str):
    """Delete a patient record"""
    db = DbController()
    db.connect()
    
    try:
        record_id = f"patient:{patient_id}"
        result = db.delete(record_id)
        return result
    except Exception as e:
        print(f"Error deleting patient: {e}")
        return None
    finally:
        db.close()


def create_patient(patient_data: dict):
    """Create a new patient record"""
    db = DbController()
    db.connect()
    
    try:
        # Generate a new demographic_no if not provided
        if not patient_data.get("demographic_no"):
            # Get the highest existing demographic_no and increment
            results = db.select_many('patient')
            if results and isinstance(results, list) and len(results) > 0:
                existing_ids = [int(p.get('demographic_no', 0)) for p in results if p.get('demographic_no')]
                new_id = max(existing_ids) + 1 if existing_ids else 1000
            else:
                new_id = 1000
            patient_data["demographic_no"] = str(new_id)
        
        # Create Patient object
        patient = Patient(
            demographic_no=patient_data["demographic_no"],
            first_name=patient_data.get("first_name"),
            last_name=patient_data.get("last_name"),
            date_of_birth=patient_data.get("date_of_birth"),
            location=tuple(patient_data.get("location", [])),
            sex=patient_data.get("sex"),
            phone=patient_data.get("phone"),
            email=patient_data.get("email")
        )
        
        result = store_patient(db, patient)
        
        # Handle different result structures
        if result and isinstance(result, list) and len(result) > 0:
            if 'result' in result[0]:
                return serialize_patient(result[0]['result'])
            else:
                return serialize_patient(result[0])
        elif result and isinstance(result, dict):
            return serialize_patient(result)
        return None
    except Exception as e:
        print(f"Error creating patient: {e}")
        return None
    finally:
        db.close()


def get_all_patients():
    """Get all patients from the database"""
    db = DbController()
    db.connect()
    
    try:
        results = db.select_many('patient')
        
        # Handle different result structures
        if results and isinstance(results, list) and len(results) > 0:
            # If the first result has a 'result' key, extract the actual data
            if isinstance(results[0], dict) and 'result' in results[0]:
                patients = results[0]['result']
            else:
                patients = results
            
            if isinstance(patients, list):
                return [serialize_patient(patient) for patient in patients]
            else:
                return []
        return []
    except Exception as e:
        print(f"Error getting all patients: {e}")
        return []
    finally:
        db.close()


#create_schema()
