"""
Simple test script to verify the patient CRUD API endpoints
"""
import requests
import json
from settings import BASE_URL

def test_api():
    print("Testing Patient CRUD API endpoints...")
    print(f"Base URL: {BASE_URL}")
    print("-" * 50)
    
    # Test 1: Get all patients
    print("1. Testing GET /patients")
    try:
        response = requests.get(f"{BASE_URL}/patients")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            patients = response.json()
            print(f"Found {len(patients)} patients")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("-" * 50)
    
    # Test 2: Create a test patient
    print("2. Testing POST /patients")
    test_patient = {
        "first_name": "Test",
        "last_name": "Patient",
        "date_of_birth": "1990-01-01",
        "sex": "M",
        "phone": "555-1234",
        "email": "test@example.com",
        "location": ["Test City", "Test State", "Test Country", "12345"]
    }
    
    try:
        response = requests.post(f"{BASE_URL}/patients", json=test_patient)
        print(f"Status: {response.status_code}")
        if response.status_code == 201:
            created_patient = response.json()
            print(f"Created patient: {created_patient.get('first_name')} {created_patient.get('last_name')}")
            patient_id = created_patient.get('demographic_no')
            
            # Test 3: Get the created patient
            print("\n3. Testing GET /patients/{id}")
            response = requests.get(f"{BASE_URL}/patients/{patient_id}")
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                patient = response.json()
                print(f"Retrieved patient: {patient.get('first_name')} {patient.get('last_name')}")
            
            # Test 4: Update the patient
            print("\n4. Testing PUT /patients/{id}")
            update_data = {"phone": "555-5678"}
            response = requests.put(f"{BASE_URL}/patients/{patient_id}", json=update_data)
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                updated_patient = response.json()
                print(f"Updated patient phone: {updated_patient.get('phone')}")
            
            # Test 5: Delete the patient
            print("\n5. Testing DELETE /patients/{id}")
            response = requests.delete(f"{BASE_URL}/patients/{patient_id}")
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                print("Patient deleted successfully")
            
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("-" * 50)
    print("API test completed!")

if __name__ == "__main__":
    test_api() 