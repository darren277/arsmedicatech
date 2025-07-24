"""
Simple test script to check what's in the SurrealDB database
"""
from lib.db.surreal import DbController
from lib.models.patient import get_all_patients, get_patient_by_id
from settings import BASE_URL


def test_database():
    print("Testing database contents...")
    print("-" * 50)
    
    # Test 1: Get all patients using our function
    print("1. Getting all patients using get_all_patients()...")
    patients = get_all_patients()
    print(f"Found {len(patients)} patients")
    
    if patients:
        print("Patient IDs found:")
        for patient in patients:
            print(f"  - {patient.get('demographic_no')}: {patient.get('first_name')} {patient.get('last_name')}")
        
        # Test 2: Try to get the first patient by ID
        first_patient_id = patients[0].get('demographic_no')
        print(f"\n2. Testing get_patient_by_id with ID: {first_patient_id}")
        patient = get_patient_by_id(first_patient_id)
        if patient:
            print(f"Successfully retrieved: {patient.get('first_name')} {patient.get('last_name')}")
        else:
            print("Failed to retrieve patient")
    else:
        print("No patients found in database")
    
    # Test 3: Direct database query to see all records
    print("\n3. Direct database query to see all patient records...")
    db = DbController()
    db.connect()
    
    try:
        # Query all patient records directly
        result = db.query("SELECT * FROM patient")
        print(f"Direct query result: {result}")
        
        if result and isinstance(result, list) and len(result) > 0:
            print("Raw patient records:")
            for record in result:
                print(f"  - {record}")
        else:
            print("No records found in direct query")
            
    except Exception as e:
        print(f"Error in direct query: {e}")
    finally:
        db.close()
    
    print("-" * 50)
    print("Database test completed!")

if __name__ == "__main__":
    test_database() 