"""
Test script to create a patient and immediately retrieve it
"""
from lib.models.patient import (create_patient, get_all_patients,
                                get_patient_by_id)
from settings import BASE_URL


def test_create_and_retrieve():
    print("Testing create and retrieve patient flow...")
    print("-" * 50)
    
    # Test 1: Create a test patient
    print("1. Creating a test patient...")
    test_patient_data = {
        "first_name": "Test",
        "last_name": "Patient",
        "date_of_birth": "1990-01-01",
        "sex": "M",
        "phone": "555-1234",
        "email": "test@example.com",
        "location": ["Test City", "Test State", "Test Country", "12345"]
    }
    
    created_patient = create_patient(test_patient_data)
    if created_patient:
        print(f"Successfully created patient: {created_patient.get('first_name')} {created_patient.get('last_name')}")
        print(f"Patient ID: {created_patient.get('demographic_no')}")
        
        # Test 2: Immediately retrieve the created patient
        patient_id = created_patient.get('demographic_no')
        print(f"\n2. Retrieving patient with ID: {patient_id}")
        
        retrieved_patient = get_patient_by_id(patient_id)
        if retrieved_patient:
            print(f"Successfully retrieved patient: {retrieved_patient.get('first_name')} {retrieved_patient.get('last_name')}")
        else:
            print("Failed to retrieve the patient we just created!")
            
        # Test 3: Check if it appears in the list
        print(f"\n3. Checking if patient appears in get_all_patients()...")
        all_patients = get_all_patients()
        found_in_list = any(p.get('demographic_no') == patient_id for p in all_patients)
        if found_in_list:
            print(f"Patient {patient_id} found in patient list")
        else:
            print(f"Patient {patient_id} NOT found in patient list")
            
    else:
        print("Failed to create patient")
    
    print("-" * 50)
    print("Test completed!")

if __name__ == "__main__":
    test_create_and_retrieve() 