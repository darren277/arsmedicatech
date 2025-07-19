#!/usr/bin/env python3
"""
Script to check and initialize the database
"""

import os
import sys

# Add the parent directory to the path so we can import from lib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.db.surreal import DbController
from lib.services.user_service import UserService


def init_database():
    """Check and initialize the database"""
    print("🔧 Initializing Database")
    
    # Create user service
    user_service = UserService()
    
    try:
        print("\n1. Connecting to database...")
        user_service.connect()
        print("✅ Database connected")
        
        print("\n2. Checking if tables exist...")
        try:
            # Try to get all records from User table
            users = user_service.db.select_many('User')
            print(f"User table exists - found {len(users) if users else 0} users")
        except Exception as e:
            print(f"User table error: {e}")
        
        try:
            # Try to get all records from Session table
            sessions = user_service.db.select_many('Session')
            print(f"Session table exists - found {len(sessions) if sessions else 0} sessions")
        except Exception as e:
            print(f"Session table error: {e}")
        
        print("\n3. Creating default admin user if no users exist...")
        success, message = user_service.create_default_admin()
        print(f"Default admin creation: {success} - {message}")
        
        print("\n4. Getting all users after initialization...")
        users = user_service.get_all_users()
        print(f"Total users in database: {len(users)}")
        for i, user in enumerate(users, 1):
            print(f"  {i}. Username: {user.username}")
            print(f"     ID: {user.id}")
            print(f"     Email: {user.email}")
            print(f"     Role: {user.role}")
            print(f"     Active: {user.is_active}")
            print()
        
        if users:
            print("\n5. Testing user lookup...")
            test_user = users[0]
            print(f"Testing lookup for user: {test_user.username} (ID: {test_user.id})")
            
            found_user = user_service.get_user_by_id(test_user.id)
            if found_user:
                print(f"✅ User lookup successful: {found_user.username}")
            else:
                print(f"❌ User lookup failed for ID: {test_user.id}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        user_service.close()

if __name__ == "__main__":
    init_database() 