"""
Test script to check and create database schema
"""
from lib.db.surreal import DbController
from lib.models.patient import create_schema
from settings import BASE_URL


def test_schema():
    print("Testing database schema...")
    print("-" * 50)
    
    # Test 1: Check if schema exists
    print("1. Checking current database state...")
    db = DbController()
    db.connect()
    
    try:
        # Try to query the patient table
        result = db.query("SELECT * FROM patient LIMIT 1")
        print(f"Patient table query result: {result}")
        
        if result and isinstance(result, list) and len(result) > 0:
            print("Patient table exists and is accessible")
        else:
            print("Patient table might not exist or be empty")
            
    except Exception as e:
        print(f"Error querying patient table: {e}")
        print("This might indicate the schema doesn't exist")
    
    db.close()
    
    # Test 2: Create schema
    print("\n2. Creating schema...")
    try:
        create_schema()
        print("Schema creation completed")
    except Exception as e:
        print(f"Error creating schema: {e}")
    
    # Test 3: Check again after schema creation
    print("\n3. Checking database state after schema creation...")
    db = DbController()
    db.connect()
    
    try:
        result = db.query("SELECT * FROM patient LIMIT 1")
        print(f"Patient table query result after schema creation: {result}")
        
        # Also check table definition
        schema_result = db.query("INFO FOR TABLE patient")
        print(f"Patient table schema: {schema_result}")
        
    except Exception as e:
        print(f"Error after schema creation: {e}")
    finally:
        db.close()
    
    print("-" * 50)
    print("Schema test completed!")

if __name__ == "__main__":
    test_schema() 