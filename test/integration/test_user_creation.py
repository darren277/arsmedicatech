#!/usr/bin/env python3
"""
Script to test user creation and see what ID format is used
"""

import sys
import os

# Add the parent directory to the path so we can import from lib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.services.user_service import UserService

def test_user_creation():
    """Test user creation and see what ID format is used"""
    print("🧪 Testing User Creation")
    
    # Create user service
    user_service = UserService()
    
    try:
        print("\n1. Connecting to database...")
        user_service.connect()
        print("✅ Database connected")
        
        print("\n2. Creating test user...")
        success, message, user = user_service.create_user(
            username="testuser123",
            email="testuser123@example.com",
            password="TestPass123!",
            first_name="Test",
            last_name="User",
            role="provider"
        )
        
        print(f"Success: {success}")
        print(f"Message: {message}")
        if user:
            print(f"User ID: {user.id}")
            print(f"Username: {user.username}")
            print(f"Email: {user.email}")
            print(f"Role: {user.role}")
        
        if success and user:
            print("\n3. Testing authentication...")
            auth_success, auth_message, session = user_service.authenticate_user(
                "testuser123",
                "TestPass123!"
            )
            
            print(f"Auth Success: {auth_success}")
            print(f"Auth Message: {auth_message}")
            if session:
                print(f"Session User ID: {session.user_id}")
                print(f"Session Username: {session.username}")
                print(f"Session Token: {session.token[:20]}...")
            
            print("\n4. Testing user lookup by ID...")
            found_user = user_service.get_user_by_id(user.id)
            if found_user:
                print(f"✅ User found by ID: {found_user.username}")
            else:
                print(f"❌ User not found by ID: {user.id}")
        
        print("\n5. Getting all users...")
        users = user_service.get_all_users()
        print(f"Total users in database: {len(users)}")
        for u in users:
            print(f"  - {u.username} (ID: {u.id})")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        user_service.close()

if __name__ == "__main__":
    test_user_creation() 