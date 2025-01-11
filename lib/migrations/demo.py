""""""
from lib.db.surreal import DbController
from lib.migrations.demo_utils import PatientFactory, EncounterFactory, select_n_random_rows_from_csv
from lib.models.patient import create_schema, store_patient, store_encounter


def create_n_patients(n):
    db = DbController(namespace='arsmedicatech', database='patients')

    path = r'section111validicd10-jan2025_0_sample.csv'
    for i in range(n):
        patient = PatientFactory()

        encounter = EncounterFactory()
        encounter.diagnostic_codes = select_n_random_rows_from_csv(path, 3)

        print(patient.first_name, patient.last_name, patient.date_of_birth, patient.phone, patient.sex, patient.email)
        print(patient.location)
        print(encounter.note_id, encounter.date_created, encounter.provider_id, encounter.diagnostic_codes)
        print(encounter.note_text)
        print("------")

        result = store_patient(db, patient)

        result = result[0]['result'][0]
        patient_id = str(result['id'])

        store_encounter(db, encounter, patient_id)

    db.close()



create_schema()
create_n_patients(5)


