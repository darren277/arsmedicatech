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



class SOAPNotes:
    def __init__(self, subjective: str, objective: str, assessment: str, plan: str):
        self.subjective = subjective
        self.objective = objective
        self.assessment = assessment
        self.plan = plan

    def serialize(self):
        return dict(
            subjective=self.subjective,
            objective=self.objective,
            assessment=self.assessment,
            plan=self.plan
        )

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            subjective=data.get('subjective'),
            objective=data.get('objective'),
            assessment=data.get('assessment'),
            plan=data.get('plan')
        )


class Encounter:
    def __init__(self, note_id, date_created, provider_id, soap_notes: SOAPNotes=None, additional_notes: str=None, diagnostic_codes=None):
        self.note_id = note_id
        self.date_created = date_created
        self.provider_id = provider_id
        self.soap_notes = soap_notes
        self.additional_notes = additional_notes
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
        "note_text": encounter.soap_notes.serialize() if encounter.soap_notes else encounter.additional_notes,
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

def search_encounter_history(search_term: str):
    """Performs a full-text search across all encounter notes."""
    db = DbController()
    db.connect()
    
    print("ATTEMPTING SEARCH", search_term)
    
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
    print(f"[DEBUG] Getting patient by ID: {patient_id}")
    db = DbController()
    db.connect()
    
    try:
        # Use a direct query instead of select method
        query = "SELECT * FROM patient WHERE demographic_no = $patient_id"
        params = {"patient_id": patient_id}
        
        print(f"[DEBUG] Executing query: {query} with params: {params}")
        result = db.query(query, params)
        print(f"[DEBUG] Query result: {result}")
        
        # Handle the result structure
        if result and isinstance(result, list) and len(result) > 0:
            # Extract the first (and should be only) patient
            patient_data = result[0]
            if isinstance(patient_data, dict) and 'result' in patient_data:
                patient_data = patient_data['result'][0] if patient_data['result'] else None
            
            if patient_data:
                serialized_result = serialize_patient(patient_data)
                print(f"[DEBUG] Serialized result: {serialized_result}")
                return serialized_result
            else:
                print("[DEBUG] No patient found in query result")
                return None
        else:
            print("[DEBUG] No patient found")
            return None
    except Exception as e:
        print(f"[DEBUG] Error getting patient: {e}")
        return None
    finally:
        db.close()


def update_patient(patient_id: str, patient_data: dict):
    """Update a patient record with only the provided fields, supporting PATCH/partial updates."""
    print(f"[DEBUG] Updating patient with ID: {patient_id}")
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
            print("[DEBUG] No valid fields to update.")
            return None

        set_clause = ", ".join([f"{k} = ${k}" for k in update_data.keys()])
        query = f"UPDATE patient SET {set_clause} WHERE demographic_no = $patient_id RETURN *"
        params = {**update_data, "patient_id": patient_id}
        
        print(f"[DEBUG] Executing update query: {query} with params: {params}")
        result = db.query(query, params)
        print(f"[DEBUG] Update result: {result}")
        
        # Handle the result structure
        if result and isinstance(result, list) and len(result) > 0:
            patient_data = result[0]
            if isinstance(patient_data, dict) and 'result' in patient_data:
                patient_data = patient_data['result'][0] if patient_data['result'] else None
            
            if patient_data:
                serialized_result = serialize_patient(patient_data)
                print(f"[DEBUG] Serialized update result: {serialized_result}")
                return serialized_result
            else:
                print("[DEBUG] No patient found in update result")
                return None
        else:
            print("[DEBUG] Update failed or no patient found")
            return None
    except Exception as e:
        print(f"[DEBUG] Error updating patient: {e}")
        return None
    finally:
        db.close()


def delete_patient(patient_id: str):
    """Delete a patient record"""
    print(f"[DEBUG] Deleting patient with ID: {patient_id}")
    db = DbController()
    db.connect()
    
    try:
        # Use a direct DELETE query
        query = "DELETE FROM patient WHERE demographic_no = $patient_id"
        params = {"patient_id": patient_id}
        
        print(f"[DEBUG] Executing delete query: {query} with params: {params}")
        result = db.query(query, params)
        print(f"[DEBUG] Delete result: {result}")
        
        # Check if the delete was successful
        if result and isinstance(result, list) and len(result) > 0:
            # Check if any records were actually deleted
            delete_info = result[0]
            if isinstance(delete_info, dict) and 'result' in delete_info:
                deleted_count = len(delete_info['result']) if delete_info['result'] else 0
                print(f"[DEBUG] Deleted {deleted_count} records")
                return deleted_count > 0
            else:
                print("[DEBUG] Delete result structure unexpected")
                return False
        else:
            print("[DEBUG] No delete result")
            return False
    except Exception as e:
        print(f"[DEBUG] Error deleting patient: {e}")
        return None
    finally:
        db.close()


def create_patient(patient_data: dict):
    """Create a new patient record"""
    print(f"[DEBUG] Creating patient with data: {patient_data}")
    db = DbController()
    db.connect()
    
    try:
        # Generate a new demographic_no if not provided
        if not patient_data.get("demographic_no"):
            print("[DEBUG] No demographic_no provided, generating new one...")
            # Get the highest existing demographic_no and increment
            results = db.select_many('patient')
            if results and isinstance(results, list) and len(results) > 0:
                existing_ids = [int(p.get('demographic_no', 0)) for p in results if p.get('demographic_no')]
                new_id = max(existing_ids) + 1 if existing_ids else 1000
            else:
                new_id = 1000
            patient_data["demographic_no"] = str(new_id)
            print(f"[DEBUG] Generated demographic_no: {new_id}")
        
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
        
        print(f"[DEBUG] Created Patient object: {patient}")
        result = store_patient(db, patient)
        print(f"[DEBUG] Store patient result: {result}")
        
        # Handle different result structures
        if result and isinstance(result, list) and len(result) > 0:
            if 'result' in result[0]:
                final_result = serialize_patient(result[0]['result'])
            else:
                final_result = serialize_patient(result[0])
        elif result and isinstance(result, dict):
            final_result = serialize_patient(result)
        else:
            final_result = None
        
        print(f"[DEBUG] Final result: {final_result}")
        return final_result
    except Exception as e:
        print(f"[DEBUG] Error creating patient: {e}")
        return None
    finally:
        db.close()


def get_all_patients():
    """Get all patients from the database"""
    db = DbController()
    db.connect()
    
    try:
        print("[DEBUG] Getting all patients from database...")
        results = db.select_many('patient')
        print(f"[DEBUG] Raw results: {results}")
        
        # Handle different result structures
        if results and isinstance(results, list) and len(results) > 0:
            # If the first result has a 'result' key, extract the actual data
            if isinstance(results[0], dict) and 'result' in results[0]:
                patients = results[0]['result']
            else:
                patients = results
            
            print(f"[DEBUG] Processed patients: {patients}")
            
            if isinstance(patients, list):
                serialized_patients = [serialize_patient(patient) for patient in patients]
                print(f"[DEBUG] Serialized patients: {serialized_patients}")
                return serialized_patients
            else:
                print("[DEBUG] Patients is not a list")
                return []
        else:
            print("[DEBUG] No results or empty results")
            return []
    except Exception as e:
        print(f"[DEBUG] Error getting all patients: {e}")
        return []
    finally:
        db.close()


def get_all_encounters():
    """Get all encounters from the database"""
    db = DbController()
    db.connect()
    
    try:
        print("[DEBUG] Getting all encounters from database...")
        results = db.select_many('encounter')
        print(f"[DEBUG] Raw encounter results: {results}")
        
        # Handle different result structures
        if results and isinstance(results, list) and len(results) > 0:
            # If the first result has a 'result' key, extract the actual data
            if isinstance(results[0], dict) and 'result' in results[0]:
                encounters = results[0]['result']
            else:
                encounters = results
            
            print(f"[DEBUG] Processed encounters: {encounters}")
            
            if isinstance(encounters, list):
                serialized_encounters = [serialize_encounter(encounter) for encounter in encounters]
                print(f"[DEBUG] Serialized encounters: {serialized_encounters}")
                return serialized_encounters
            else:
                print("[DEBUG] Encounters is not a list")
                return []
        else:
            print("[DEBUG] No encounter results or empty results")
            return []
    except Exception as e:
        print(f"[DEBUG] Error getting all encounters: {e}")
        return []
    finally:
        db.close()


def get_encounter_by_id(encounter_id: str):
    """Get an encounter by its note_id"""
    print(f"[DEBUG] Getting encounter by ID: {encounter_id}")
    db = DbController()
    db.connect()
    
    try:
        query = "SELECT * FROM encounter WHERE note_id = $encounter_id"
        params = {"encounter_id": encounter_id}
        
        print(f"[DEBUG] Executing encounter query: {query} with params: {params}")
        result = db.query(query, params)
        print(f"[DEBUG] Encounter query result: {result}")
        
        # Handle the result structure
        if result and isinstance(result, list) and len(result) > 0:
            encounter_data = result[0]
            if isinstance(encounter_data, dict) and 'result' in encounter_data:
                encounter_data = encounter_data['result'][0] if encounter_data['result'] else None
            
            if encounter_data:
                serialized_result = serialize_encounter(encounter_data)
                print(f"[DEBUG] Serialized encounter result: {serialized_result}")
                return serialized_result
            else:
                print("[DEBUG] No encounter found in query result")
                return None
        else:
            print("[DEBUG] No encounter found")
            return None
    except Exception as e:
        print(f"[DEBUG] Error getting encounter: {e}")
        return None
    finally:
        db.close()


def get_encounters_by_patient(patient_id: str):
    """Get all encounters for a specific patient"""
    print(f"[DEBUG] Getting encounters for patient: {patient_id}")
    db = DbController()
    db.connect()
    
    try:
        query = "SELECT * FROM encounter WHERE patient = $patient_id ORDER BY date_created DESC"
        params = {"patient_id": f"patient:{patient_id}"}
        
        print(f"[DEBUG] Executing patient encounters query: {query} with params: {params}")
        result = db.query(query, params)
        print(f"[DEBUG] Patient encounters query result: {result}")
        
        # Handle the result structure
        if result and isinstance(result, list) and len(result) > 0:
            encounters_data = result[0]
            if isinstance(encounters_data, dict) and 'result' in encounters_data:
                encounters = encounters_data['result']
            else:
                encounters = result
            
            if isinstance(encounters, list):
                serialized_encounters = [serialize_encounter(encounter) for encounter in encounters]
                print(f"[DEBUG] Serialized patient encounters: {serialized_encounters}")
                return serialized_encounters
            else:
                print("[DEBUG] Patient encounters is not a list")
                return []
        else:
            print("[DEBUG] No patient encounters found")
            return []
    except Exception as e:
        print(f"[DEBUG] Error getting patient encounters: {e}")
        return []
    finally:
        db.close()


def create_encounter(encounter_data: dict, patient_id: str):
    """Create a new encounter record"""
    print(f"[DEBUG] Creating encounter with data: {encounter_data}")
    db = DbController()
    db.connect()
    
    try:
        # Generate a new note_id if not provided
        if not encounter_data.get("note_id"):
            print("[DEBUG] No note_id provided, generating new one...")
            results = db.select_many('encounter')
            if results and isinstance(results, list) and len(results) > 0:
                existing_ids = [int(e.get('note_id', 0)) for e in results if e.get('note_id')]
                new_id = max(existing_ids) + 1 if existing_ids else 1000
            else:
                new_id = 1000
            encounter_data["note_id"] = str(new_id)
            print(f"[DEBUG] Generated note_id: {new_id}")
        
        # Create Encounter object
        encounter = Encounter(
            note_id=encounter_data["note_id"],
            date_created=encounter_data.get("date_created"),
            provider_id=encounter_data.get("provider_id"),
            additional_notes=encounter_data.get("note_text"),
            diagnostic_codes=encounter_data.get("diagnostic_codes", [])
        )
        
        print(f"[DEBUG] Created Encounter object: {encounter}")
        result = store_encounter(db, encounter, f"patient:{patient_id}")
        print(f"[DEBUG] Store encounter result: {result}")
        
        # Handle different result structures
        if result and isinstance(result, list) and len(result) > 0:
            if 'result' in result[0]:
                final_result = serialize_encounter(result[0]['result'])
            else:
                final_result = serialize_encounter(result[0])
        elif result and isinstance(result, dict):
            final_result = serialize_encounter(result)
        else:
            final_result = None
        
        print(f"[DEBUG] Final encounter result: {final_result}")
        return final_result
    except Exception as e:
        print(f"[DEBUG] Error creating encounter: {e}")
        return None
    finally:
        db.close()


def update_encounter(encounter_id: str, encounter_data: dict):
    """Update an encounter record with only the provided fields"""
    print(f"[DEBUG] Updating encounter with ID: {encounter_id}")
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
            print("[DEBUG] No valid fields to update for encounter.")
            return None

        set_clause = ", ".join([f"{k} = ${k}" for k in update_data.keys()])
        query = f"UPDATE encounter SET {set_clause} WHERE note_id = $encounter_id RETURN *"
        params = {**update_data, "encounter_id": encounter_id}
        
        print(f"[DEBUG] Executing encounter update query: {query} with params: {params}")
        result = db.query(query, params)
        print(f"[DEBUG] Encounter update result: {result}")
        
        # Handle the result structure
        if result and isinstance(result, list) and len(result) > 0:
            encounter_data = result[0]
            if isinstance(encounter_data, dict) and 'result' in encounter_data:
                encounter_data = encounter_data['result'][0] if encounter_data['result'] else None
            
            if encounter_data:
                serialized_result = serialize_encounter(encounter_data)
                print(f"[DEBUG] Serialized encounter update result: {serialized_result}")
                return serialized_result
            else:
                print("[DEBUG] No encounter found in update result")
                return None
        else:
            print("[DEBUG] Encounter update failed or no encounter found")
            return None
    except Exception as e:
        print(f"[DEBUG] Error updating encounter: {e}")
        return None
    finally:
        db.close()


def delete_encounter(encounter_id: str):
    """Delete an encounter record"""
    print(f"[DEBUG] Deleting encounter with ID: {encounter_id}")
    db = DbController()
    db.connect()
    
    try:
        query = "DELETE FROM encounter WHERE note_id = $encounter_id"
        params = {"encounter_id": encounter_id}
        
        print(f"[DEBUG] Executing encounter delete query: {query} with params: {params}")
        result = db.query(query, params)
        print(f"[DEBUG] Encounter delete result: {result}")
        
        # Check if the delete was successful
        if result and isinstance(result, list) and len(result) > 0:
            delete_info = result[0]
            if isinstance(delete_info, dict) and 'result' in delete_info:
                deleted_count = len(delete_info['result']) if delete_info['result'] else 0
                print(f"[DEBUG] Deleted {deleted_count} encounter records")
                return deleted_count > 0
            else:
                print("[DEBUG] Encounter delete result structure unexpected")
                return False
        else:
            print("[DEBUG] No encounter delete result")
            return False
    except Exception as e:
        print(f"[DEBUG] Error deleting encounter: {e}")
        return None
    finally:
        db.close()


#create_schema()
