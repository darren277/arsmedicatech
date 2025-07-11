"""
Minimal test for database save operation
"""

import os
import sys

# Add the lib directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

def test_db_save():
    """Test just the database save operation"""
    print("🔍 Testing Database Save Operation")
    print("=" * 50)
    
    try:
        from db.surreal import DbController
        from services.encryption import get_encryption_service
        
        # Initialize
        db = DbController()
        db.connect()
        encryption_service = get_encryption_service()
        
        # Test data
        test_user_id = "user:test123"
        test_api_key = "sk-test1234567890123456789012345678901234567890123456789012345678901"  # Exactly 51 chars
        encrypted_key = encryption_service.encrypt_api_key(test_api_key)
        
        print(f"Test user ID: {test_user_id}")
        print(f"Test API key: {test_api_key[:10]}...")
        print(f"Encrypted key: {encrypted_key[:20]}...")
        
        # Test 1: Direct database create
        print("\n1️⃣ Testing direct database create...")
        test_data = {
            'user_id': test_user_id,
            'openai_api_key': encrypted_key,
            'created_at': '2024-01-01T00:00:00',
            'updated_at': '2024-01-01T00:00:00'
        }
        
        create_result = db.create('UserSettings', test_data)
        print(f"Create result: {create_result}")
        
        if create_result and isinstance(create_result, dict) and create_result.get('id'):
            record_id = create_result['id']
            print(f"Created record ID: {record_id}")
            
            # Test 2: Query the created record
            print("\n2️⃣ Querying created record...")
            query_result = db.query(
                "SELECT * FROM UserSettings WHERE user_id = $user_id",
                {"user_id": test_user_id}
            )
            print(f"Query result: {query_result}")
            
            if query_result and isinstance(query_result, list) and len(query_result) > 0:
                db_record = query_result[0]
                print(f"DB record ID: {db_record.get('id')}")
                print(f"DB user_id: {db_record.get('user_id')}")
                print(f"DB openai_api_key: {db_record.get('openai_api_key', 'None')[:20] if db_record.get('openai_api_key') else 'None'}...")
                
                # Test 3: Decrypt the stored key
                print("\n3️⃣ Testing decryption...")
                stored_encrypted = db_record.get('openai_api_key', '')
                if stored_encrypted:
                    decrypted = encryption_service.decrypt_api_key(stored_encrypted)
                    print(f"Decrypted key: {decrypted[:10]}...")
                    print(f"Matches original: {decrypted == test_api_key}")
                else:
                    print("No encrypted key found in database!")
            
            # Test 4: Update the record
            print("\n4️⃣ Testing update...")
            new_api_key = "sk-new1234567890123456789012345678901234567890123456789012345678901"  # Exactly 51 chars
            new_encrypted = encryption_service.encrypt_api_key(new_api_key)
            
            update_data = {
                'openai_api_key': new_encrypted,
                'updated_at': '2024-01-02T00:00:00'
            }
            
            update_result = db.update(record_id, update_data)
            print(f"Update result: {update_result}")
            
            # Test 5: Query after update
            print("\n5️⃣ Querying after update...")
            updated_query = db.query(
                "SELECT * FROM UserSettings WHERE user_id = $user_id",
                {"user_id": test_user_id}
            )
            print(f"Updated query result: {updated_query}")
            
            if updated_query and isinstance(updated_query, list) and len(updated_query) > 0:
                updated_record = updated_query[0]
                updated_encrypted = updated_record.get('openai_api_key', '')
                if updated_encrypted:
                    updated_decrypted = encryption_service.decrypt_api_key(updated_encrypted)
                    print(f"Updated decrypted key: {updated_decrypted[:10]}...")
                    print(f"Matches new key: {updated_decrypted == new_api_key}")
            
            # Clean up
            print("\n6️⃣ Cleaning up...")
            delete_result = db.delete(record_id)
            print(f"Delete result: {delete_result}")
        
        db.close()
        return True
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_db_save()
    if success:
        print("\n✅ Database save test completed!")
    else:
        print("\n❌ Database save test failed!") 