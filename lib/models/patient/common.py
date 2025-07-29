"""
Common definitions for Patient and Encounter models in SurrealDB.
"""
from typing import Any, Dict, List

from lib.db.surreal import DbController
from lib.models.patient.encounter_model import Encounter
from lib.models.patient.patient_model import Patient

PatientDict = Dict[str, str | int | List[Any] | None]  # Define a type for patient dictionaries

EncounterDict = Dict[str, str | int | List[Any] | None]  # Define a type for encounter dictionaries



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
