"""
Debug script to test settings functionality
"""

import os
import sys

# Add the lib directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

def test_settings_flow():
    """Test the complete settings flow"""
    print("🔍 Testing Settings Flow")
    print("=" * 50)
    
    # Check environment
    encryption_key = os.getenv('ENCRYPTION_KEY')
    if not encryption_key:
        print("❌ ENCRYPTION_KEY environment variable not set")
        print("   Please set: export ENCRYPTION_KEY='your-secure-key-here'")
        return False
    
    print(f"✅ ENCRYPTION_KEY is set (length: {len(encryption_key)})")
    
    try:
        from models.user_settings import UserSettings
        from services.user_service import UserService

        # Initialize service
        user_service = UserService()
        user_service.connect()
        
        # Test user ID (replace with actual user ID from your database)
        test_user_id = "user:test123"  # Change this to a real user ID
        
        print(f"\n📝 Testing with user ID: {test_user_id}")
        
        # Test 1: Get initial settings
        print("\n1️⃣ Getting initial settings...")
        settings = user_service.get_user_settings(test_user_id)
        if settings:
            print(f"   ✅ Settings found: {settings.id}")
            print(f"   Has API key: {settings.has_openai_api_key()}")
        else:
            print("   ❌ No settings found")
        
        # Test 2: Update with valid API key
        print("\n2️⃣ Testing valid API key update...")
        test_api_key = "sk-test123456789012345678901234567890123456789012345678901234567890"
        success, message = user_service.update_openai_api_key(test_user_id, test_api_key)
        print(f"   Result: {success} - {message}")
        
        if success:
            # Test 3: Verify API key was saved
            print("\n3️⃣ Verifying API key was saved...")
            saved_key = user_service.get_openai_api_key(test_user_id)
            has_key = user_service.has_openai_api_key(test_user_id)
            print(f"   Retrieved key length: {len(saved_key) if saved_key else 0}")
            print(f"   Has API key: {has_key}")
            
            # Test 4: Remove API key
            print("\n4️⃣ Testing API key removal...")
            success, message = user_service.update_openai_api_key(test_user_id, "")
            print(f"   Result: {success} - {message}")
            
            if success:
                # Test 5: Verify API key was removed
                print("\n5️⃣ Verifying API key was removed...")
                saved_key = user_service.get_openai_api_key(test_user_id)
                has_key = user_service.has_openai_api_key(test_user_id)
                print(f"   Retrieved key length: {len(saved_key) if saved_key else 0}")
                print(f"   Has API key: {has_key}")
        
        user_service.close()
        return True
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_settings_flow()
    if success:
        print("\n✅ Settings flow test completed successfully!")
        print("\n💡 If you're still having issues in the web app:")
        print("   1. Check the server logs for DEBUG messages")
        print("   2. Verify the user ID is correct")
        print("   3. Check database connectivity")
        print("   4. Ensure ENCRYPTION_KEY is set in production")
    else:
        print("\n❌ Settings flow test failed!")
        print("   Check the errors above and fix them.") 