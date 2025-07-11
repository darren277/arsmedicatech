import os
import sys

# Add the lib directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

def test_encryption_key():
    """Test if encryption key is available"""
    print("=== Testing Encryption Key ===")
    
    # Check environment variable
    encryption_key = os.getenv('ENCRYPTION_KEY')
    if encryption_key:
        print(f"✅ ENCRYPTION_KEY is set (length: {len(encryption_key)})")
        print(f"   First 10 chars: {encryption_key[:10]}...")
    else:
        print("❌ ENCRYPTION_KEY is not set")
        return False
    
    # Test encryption service
    try:
        from services.encryption import get_encryption_service
        encryption_service = get_encryption_service()
        print("✅ Encryption service initialized successfully")
        
        # Test encryption/decryption
        test_data = "test-api-key-123"
        encrypted = encryption_service.encrypt_api_key(test_data)
        decrypted = encryption_service.decrypt_api_key(encrypted)
        
        if decrypted == test_data:
            print("✅ Encryption/decryption test passed")
        else:
            print(f"❌ Encryption/decryption test failed: {decrypted} != {test_data}")
            return False
            
    except Exception as e:
        print(f"❌ Encryption service error: {e}")
        return False
    
    return True

def test_user_settings():
    """Test user settings functionality"""
    print("\n=== Testing User Settings ===")
    
    try:
        from models.user_settings import UserSettings
        
        # Test settings creation
        settings = UserSettings(user_id="test-user-123")
        print("✅ UserSettings model created")
        
        # Test API key validation
        valid_key = "sk-test123456789012345678901234567890123456789012345678901234567890"
        invalid_key = "invalid-key"
        
        valid, msg = UserSettings.validate_openai_api_key(valid_key)
        if valid:
            print("✅ Valid API key validation passed")
        else:
            print(f"❌ Valid API key validation failed: {msg}")
            return False
        
        valid, msg = UserSettings.validate_openai_api_key(invalid_key)
        if not valid:
            print("✅ Invalid API key validation passed")
        else:
            print(f"❌ Invalid API key validation failed: {msg}")
            return False
            
    except Exception as e:
        print(f"❌ UserSettings error: {e}")
        return False
    
    return True

def test_user_service():
    """Test user service settings methods"""
    print("\n=== Testing User Service ===")
    
    try:
        from services.user_service import UserService
        
        user_service = UserService()
        print("✅ UserService created")
        
        # Test settings methods exist
        if hasattr(user_service, 'get_user_settings'):
            print("✅ get_user_settings method exists")
        else:
            print("❌ get_user_settings method missing")
            return False
            
        if hasattr(user_service, 'update_openai_api_key'):
            print("✅ update_openai_api_key method exists")
        else:
            print("❌ update_openai_api_key method missing")
            return False
            
        if hasattr(user_service, 'get_openai_api_key'):
            print("✅ get_openai_api_key method exists")
        else:
            print("❌ get_openai_api_key method missing")
            return False
            
    except Exception as e:
        print(f"❌ UserService error: {e}")
        return False
    
    return True

def main():
    """Run all tests"""
    print("🔍 Debugging Settings System")
    print("=" * 50)
    
    tests = [
        test_encryption_key,
        test_user_settings,
        test_user_service
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
            results.append(False)
    
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"✅ All {total} tests passed!")
        print("\n💡 If you're still having issues, check:")
        print("   1. Database connection")
        print("   2. User authentication")
        print("   3. Network connectivity")
        print("   4. Server logs for errors")
    else:
        print(f"❌ {total - passed} out of {total} tests failed")
        print("\n🔧 Fix the failing tests above before proceeding")

if __name__ == '__main__':
    main() 