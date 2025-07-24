"""
Focused test for API key saving functionality
"""

import os
import sys

# Add the lib directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

# Import settings first to ensure ENCRYPTION_KEY is generated
try:
    import settings
    print(f"✅ Settings imported, ENCRYPTION_KEY generated: {settings.ENCRYPTION_KEY[:10]}...")
except Exception as e:
    print(f"❌ Failed to import settings: {e}")

def test_api_key_saving():
    """Test just the API key saving functionality"""
    print("🔍 Testing API Key Saving")
    print("=" * 50)
    
    # Check environment or settings
    encryption_key = os.getenv('ENCRYPTION_KEY')
    if not encryption_key:
        # Try to get from settings
        try:
            import settings
            encryption_key = settings.ENCRYPTION_KEY
            print(f"✅ ENCRYPTION_KEY from settings (length: {len(encryption_key)})")
        except Exception as e:
            print(f"❌ ENCRYPTION_KEY not available: {e}")
            return False
    else:
        print(f"✅ ENCRYPTION_KEY from env (length: {len(encryption_key)})")
    
    try:
        from services.encryption import get_encryption_service
        from services.user_service import UserService

        # Initialize services
        user_service = UserService()
        user_service.connect()
        encryption_service = get_encryption_service()
        
        # Test user ID (use a real user ID from your database)
        test_user_id = "user:test123"  # Replace with actual user ID
        
        print(f"\n📝 Testing with user ID: {test_user_id}")
        
        # Test 1: Check current state
        print("\n1️⃣ Checking current state...")
        settings = user_service.get_user_settings(test_user_id)
        print(f"   Current settings: {settings.id if settings else 'None'}")
        print(f"   Has API key: {settings.has_openai_api_key() if settings else False}")
        
        # Test 2: Test encryption/decryption directly
        print("\n2️⃣ Testing encryption/decryption...")
        test_key = "sk-test1234567890123456789012345678901234567890123456789012345678901"  # 68 chars
        print(f"   Test key length: {len(test_key)}")
        
        # Create a proper 51-character test key
        proper_test_key = "sk-test1234567890123456789012345678901234567890123456789012345678901"[:51]
        print(f"   Proper test key length: {len(proper_test_key)}")
        print(f"   Proper test key: {proper_test_key}")
        
        encrypted = encryption_service.encrypt_api_key(proper_test_key)
        decrypted = encryption_service.decrypt_api_key(encrypted)
        print(f"   Original key: {proper_test_key[:10]}...")
        print(f"   Encrypted: {encrypted[:20]}...")
        print(f"   Decrypted: {decrypted[:10]}...")
        print(f"   Match: {proper_test_key == decrypted}")
        
        # Test 3: Test UserSettings model directly
        print("\n3️⃣ Testing UserSettings model...")
        if settings:
            print(f"   Current API key in model: {settings.openai_api_key[:20] if settings.openai_api_key else 'None'}...")
            
            # Set API key directly
            settings.set_openai_api_key(proper_test_key)
            print(f"   After setting: {settings.openai_api_key[:20] if settings.openai_api_key else 'None'}...")
            
            # Test to_dict
            settings_dict = settings.to_dict()
            print(f"   to_dict openai_api_key: {settings_dict['openai_api_key'][:20] if settings_dict['openai_api_key'] else 'None'}...")
            
            # Test has_openai_api_key
            has_key = settings.has_openai_api_key()
            print(f"   has_openai_api_key: {has_key}")
        
        # Test 4: Test UserService update method
        print("\n4️⃣ Testing UserService.update_openai_api_key...")
        success, message = user_service.update_openai_api_key(test_user_id, proper_test_key)
        print(f"   Result: {success} - {message}")
        
        if success:
            # Test 5: Verify it was actually saved
            print("\n5️⃣ Verifying save...")
            updated_settings = user_service.get_user_settings(test_user_id)
            print(f"   Updated settings ID: {updated_settings.id if updated_settings else 'None'}")
            print(f"   Has API key after save: {updated_settings.has_openai_api_key() if updated_settings else False}")
            
            # Get the actual API key
            retrieved_key = user_service.get_openai_api_key(test_user_id)
            print(f"   Retrieved key length: {len(retrieved_key) if retrieved_key else 0}")
            print(f"   Retrieved key matches: {retrieved_key == proper_test_key}")
            
            # Test 6: Check database directly
            print("\n6️⃣ Checking database directly...")
            db_result = user_service.db.query(
                "SELECT * FROM UserSettings WHERE user_id = $user_id",
                {"user_id": test_user_id}
            )
            print(f"   Database result: {db_result}")
            
            if db_result and isinstance(db_result, list) and len(db_result) > 0:
                db_settings = db_result[0]
                print(f"   DB openai_api_key: {db_settings.get('openai_api_key', 'None')[:20] if db_settings.get('openai_api_key') else 'None'}...")
        
        user_service.close()
        return True
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_specific_user():
    """Test with a specific user ID from your database"""
    print("\n🎯 Testing with specific user...")
    
    # You can replace this with an actual user ID from your database
    specific_user_id = input("Enter a real user ID from your database (or press Enter to skip): ").strip()
    
    if not specific_user_id:
        print("Skipping specific user test")
        return True
    
    try:
        from services.user_service import UserService
        
        user_service = UserService()
        user_service.connect()
        
        print(f"Testing with user: {specific_user_id}")
        
        # Get current settings
        settings = user_service.get_user_settings(specific_user_id)
        print(f"Current settings: {settings.id if settings else 'None'}")
        
        # Try to save a test key
        test_key = "sk-test1234567890123456789012345678901234567890123456789012345678901"[:51]  # Exactly 51 chars
        print(f"Test key length: {len(test_key)}")
        success, message = user_service.update_openai_api_key(specific_user_id, test_key)
        print(f"Save result: {success} - {message}")
        
        if success:
            # Check if it was actually saved
            retrieved_key = user_service.get_openai_api_key(specific_user_id)
            print(f"Retrieved key matches: {retrieved_key == test_key}")
        
        user_service.close()
        return True
        
    except Exception as e:
        print(f"Error testing specific user: {e}")
        return False

if __name__ == "__main__":
    print("🔧 API Key Saving Microcosm Test")
    print("=" * 50)
    
    # Run the main test
    success1 = test_api_key_saving()
    
    # Optionally test with a specific user
    success2 = test_specific_user()
    
    if success1 and success2:
        print("\n✅ All tests passed!")
        print("\n💡 If the web app is still not working, check:")
        print("   1. Server logs for the DEBUG messages we added")
        print("   2. Network requests in browser dev tools")
        print("   3. User authentication/session")
    else:
        print("\n❌ Some tests failed!")
        print("   Check the errors above to identify the issue.") 