"""
Placeholder data generation functions for testing purposes
"""
from typing import Union

from lib.db.surreal import AsyncDbController, DbController
from lib.models.patient.encounter_crud import store_encounter
from lib.models.patient.encounter_model import Encounter
from lib.models.patient.patient_crud import store_patient
from lib.models.patient.patient_model import Patient


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
