
"""
Patient Model for SurrealDB.
"""
from typing import Any, Dict, List, Optional, Tuple


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
            email: Optional[str] = None,
            organization_id: Optional[str] = None
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
        self.organization_id = organization_id
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
        statements.append('DEFINE FIELD organization_id ON patient TYPE string;')
        statements.append('DEFINE INDEX idx_patient_demographic_no ON patient FIELDS demographic_no UNIQUE;')
        return statements

