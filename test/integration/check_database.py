#!/usr/bin/env python3
"""
Script to check what users exist in the database
"""

import os
import sys

# Add the parent directory to the path so we can import from lib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.db.surreal import DbController
from lib.services.user_service import UserService


def check_database():
    """Check what users exist in the database"""
    print("🔍 Checking Database Contents")
    
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
            for i, user in enumerate(users, 1):
                print(f"  {i}. Username: {user.username}")
                print(f"     ID: {user.id}")
                print(f"     Email: {user.email}")
                print(f"     Role: {user.role}")
                print(f"     Active: {user.is_active}")
                print()
        else:
            print("  No users found in database")
        
        print("\n3. Checking database tables...")
        try:
            # Try to get all records from User table
            result = user_service.db.select_many('User')
            print(f"Raw User table contents: {result}")
        except Exception as e:
            print(f"Error getting User table: {e}")
        
        print("\n4. Checking Session table...")
        try:
            # Try to get all records from Session table
            result = user_service.db.select_many('Session')
            print(f"Raw Session table contents: {result}")
        except Exception as e:
            print(f"Error getting Session table: {e}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        user_service.close()

if __name__ == "__main__":
    check_database() 