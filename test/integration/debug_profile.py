#!/usr/bin/env python3
"""
Debug script to help identify the profile loading issue
"""

import requests
import json
import sys
import os

# Add the parent directory to the path so we can import from lib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_URL = "http://localhost:5000/api"

def debug_profile_issue():
    """Debug the profile loading issue"""
    print("🔍 Debugging Profile Loading Issue")
    
    # Test 1: Check if server is running
    print("\n1. Checking if server is running...")
    try:
        response = requests.get(f"{BASE_URL}/time")
        print(f"✅ Server is running - Status: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running or not accessible")
        print("Please start the Flask server first: python app.py")
        return False
    
    # Test 2: Check if any users exist
    print("\n2. Checking if users exist...")
    try:
        response = requests.get(f"{BASE_URL}/users/exist")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error checking users: {e}")
    
    # Test 3: Try to register a test user
    print("\n3. Registering a test user...")
    test_user = {
        "username": "debugtest",
        "email": "debugtest@example.com",
        "password": "TestPass123!",
        "first_name": "Debug",
        "last_name": "Test",
        "role": "provider"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/register", json=test_user)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 201:
            print("✅ Test user registered successfully")
        else:
            print("❌ Failed to register test user")
    except Exception as e:
        print(f"Error registering user: {e}")
    
    # Test 4: Try to login with the test user
    print("\n4. Logging in with test user...")
    login_data = {
        "username": test_user["username"],
        "password": test_user["password"]
    }
    
    try:
        response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
        
        if response.status_code == 200:
            print("✅ Login successful")
            login_response = response.json()
            token = login_response.get('token')
            user = login_response.get('user')
            print(f"Token: {token[:20] if token else 'None'}...")
            print(f"User ID: {user.get('id') if user else 'None'}")
            
            # Test 5: Try to get profile with the token
            print("\n5. Getting profile with token...")
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(f"{BASE_URL}/profile", headers=headers)
            print(f"Status: {response.status_code}")
            print(f"Response: {response.text}")
            
            if response.status_code == 200:
                print("✅ Profile retrieved successfully")
            else:
                print("❌ Failed to get profile")
        else:
            print("❌ Login failed")
    except Exception as e:
        print(f"Error during login/profile test: {e}")
    
    return True

if __name__ == "__main__":
    debug_profile_issue() 