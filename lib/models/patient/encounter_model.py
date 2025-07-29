"""
Encounter Model and SOAPNotes for SurrealDB.
"""
from typing import Any, Dict, List, Optional


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
        statements.append('DEFINE FIELD note_text ON encounter TYPE any;')
        statements.append('DEFINE FIELD note_type ON encounter TYPE string;')
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
