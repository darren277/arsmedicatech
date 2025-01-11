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
        statements.append('DEFINE TABLE encounter SCHEMAFULL;')
        statements.append('DEFINE FIELD note_id ON encounter TYPE string ASSERT $value != none;')
        statements.append('DEFINE FIELD date_created ON encounter TYPE string;')
        statements.append('DEFINE FIELD provider_id ON encounter TYPE string;')
        statements.append('DEFINE FIELD note_text ON encounter TYPE string;')
        statements.append('DEFINE FIELD diagnostic_codes ON encounter TYPE array;')

        statements.append('DEFINE FIELD patient ON encounter TYPE record<patient> ASSERT $value != none;')

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

    return result
