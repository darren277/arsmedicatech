#!/usr/bin/env python3
"""
Test script to verify user lookup by ID
"""

import os
import sys

# Add the parent directory to the path so we can import from lib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.services.user_service import UserService


def test_user_lookup():
    """Test user lookup by ID"""
    print("🧪 Testing User Lookup by ID")
    
    # Create user service
    user_service = UserService()
    
    try:
        print("\n1. Connecting to database...")
        user_service.connect()
        print("✅ Database connected")
        
        print("\n2. Getting all users...")
        users = user_service.get_all_users()
        print(f"Found {len(users)} users in database:")
        
        if users:
            test_user = users[0]  # Use the first user for testing
            print(f"\n3. Testing lookup for user: {test_user.username}")
            print(f"   User ID: {test_user.id}")
            
            # Test lookup by ID
            found_user = user_service.get_user_by_id(test_user.id)
            if found_user:
                print(f"✅ User lookup successful: {found_user.username}")
                print(f"   Found user ID: {found_user.id}")
                print(f"   Found user email: {found_user.email}")
                print(f"   Found user role: {found_user.role}")
            else:
                print(f"❌ User lookup failed for ID: {test_user.id}")
            
            # Test lookup by username to compare
            print(f"\n4. Testing lookup by username: {test_user.username}")
            found_user_by_username = user_service.get_user_by_username(test_user.username)
            if found_user_by_username:
                print(f"✅ Username lookup successful: {found_user_by_username.username}")
                print(f"   Found user ID: {found_user_by_username.id}")
            else:
                print(f"❌ Username lookup failed")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        user_service.close()

if __name__ == "__main__":
    test_user_lookup() 