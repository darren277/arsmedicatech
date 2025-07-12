"""
Utility functions and factories for generating demo data for encounters and patients.
"""
from typing import List

from faker import Faker
import factory
from lib.models.patient import Patient

from settings import logger


fake = Faker()


class PatientFactory(factory.Factory):
    class Meta:
        """
        Meta class for PatientFactory.
        """
        model = Patient

    demographic_no = factory.Faker('random_int')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    date_of_birth = factory.Faker('date_of_birth', minimum_age=18, maximum_age=65)

    phone = factory.Faker('phone_number')
    email = factory.Faker('email')
    sex = factory.Faker('random_element', elements=('M', 'F'))

    # For later use:
    location = factory.Faker('local_latlng', country_code='CA')


'''
CODE,SHORT DESCRIPTION (VALID ICD-10 FY2025),LONG DESCRIPTION (VALID ICD-10 FY2025)
A000,"Cholera due to Vibrio cholerae 01, biovar cholerae","Cholera due to Vibrio cholerae 01, biovar cholerae"
A001,"Cholera due to Vibrio cholerae 01, biovar eltor","Cholera due to Vibrio cholerae 01, biovar eltor"
A009,"Cholera, unspecified","Cholera, unspecified"
A0100,"Typhoid fever, unspecified","Typhoid fever, unspecified"
A0101,Typhoid meningitis,Typhoid meningitis
A0102,Typhoid fever with heart involvement,Typhoid fever with heart involvement
A0103,Typhoid pneumonia,Typhoid pneumonia
A0104,Typhoid arthritis,Typhoid arthritis
A0105,Typhoid osteomyelitis,Typhoid osteomyelitis
'''

path = r'section111validicd10-jan2025_0.csv'

import csv


def load_csv(path: str, n: int) -> list:
    """
    Load a CSV file and return every nth row with only the first two columns.
    :param path: The path to the CSV file.
    :param n: The step size for selecting rows (e.g., every nth row).
    :return: A list of lists, where each inner list contains the first two columns of the selected rows.
    """
    new_csv = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i % n == 0:
                new_csv.append([row[0], row[1]])
    return new_csv

#new_csv = load_csv(path, 50)
#logger.debug(len(new_csv))
#logger.debug(new_csv)


def save_csv(path: str, data: List[list]) -> None:
    """
    Save a list of lists to a CSV file.
    :param path: The path where the CSV file will be saved.
    :param data: A list of lists, where each inner list represents a row in the CSV file.
    :return: None
    """
    with open(path, 'w', newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

#save_csv(r'section111validicd10-jan2025_0_sample.csv', new_csv)



class Encounter:
    """
    Represents an encounter note for a patient.
    """
    def __init__(
            self,
            note_id: int,
            date_created: str,
            provider_id: int,
            note_text: str = None,
            diagnostic_codes: List[str] = None,
    ) -> None:
        """
        Initialize an encounter note.
        :param note_id: Unique identifier for the note.
        :param date_created: Creation date of the note in ISO format (YYYY-MM-DD).
        :param provider_id: Unique identifier for the provider who created the note.
        :param note_text: Optional text content of the note.
        :param diagnostic_codes: List of diagnostic codes associated with the encounter.
        :return: None
        """
        self.note_id = note_id
        self.date_created = date_created
        self.provider_id = provider_id
        self.note_text = note_text
        self.diagnostic_codes = diagnostic_codes
        self.status = None  # e.g., locked, signed, etc.

    def __repr__(self) -> str:
        return f"<Encounter note_id={self.note_id}, date={self.date_created}>"


def select_n_random_rows_from_csv(path: str, n: int) -> List[List[str]]:
    """
    Select n random rows from a CSV file.
    :param path: The path to the CSV file.
    :param n: The number of random rows to select.
    :return: A list of lists, where each inner list represents a row from the CSV file.
    """
    with open(path, 'r') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        return fake.random_elements(elements=rows, length=n)


class EncounterFactory(factory.Factory):
    """
    Factory for generating encounter notes with Faker.
    """
    class Meta:
        """
        Meta class for EncounterFactory.
        """
        model = Encounter

    note_id = factory.Faker('random_int')
    date_created = factory.Faker('date_of_birth', minimum_age=1, maximum_age=20)
    provider_id = factory.Faker('random_int', min=1, max=10)

    # Lorem ipsum for now...
    # TODO: Substitute with an (older, less expensive) LLM endpoint...
    note_text = factory.Faker('text', max_nb_chars=160)
