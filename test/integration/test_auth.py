#!/usr/bin/env python3
"""
Test script for the authentication system
"""

import json
import time

import requests

# Configuration
BASE_URL = "http://localhost:5000/api"
TEST_USER = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "TestPass123",
    "first_name": "Test",
    "last_name": "User"
}

def test_auth_system():
    """Test the complete authentication flow"""
    print("🧪 Testing Authentication System")
    print("=" * 50)
    
    # Test 1: Setup default admin
    print("\n1. Setting up default admin...")
    try:
        response = requests.post(f"{BASE_URL}/admin/setup")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 2: Register new user
    print("\n2. Registering new user...")
    try:
        response = requests.post(f"{BASE_URL}/auth/register", json=TEST_USER)
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        if response.status_code == 201:
            print("   ✅ User registered successfully")
        else:
            print("   ❌ User registration failed")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 3: Login with new user
    print("\n3. Logging in with new user...")
    try:
        login_data = {
            "username": TEST_USER["username"],
            "password": TEST_USER["password"]
        }
        response = requests.post(f"{BASE_URL}/auth/login", json=login_data)
        print(f"   Status: {response.status_code}")
        result = response.json()
        print(f"   Response: {result}")
        
        if response.status_code == 200:
            print("   ✅ Login successful")
            token = result.get("token")
            user_data = result.get("user")
            print(f"   Token: {token[:20]}...")
            print(f"   User: {user_data}")
        else:
            print("   ❌ Login failed")
            token = None
    except Exception as e:
        print(f"   Error: {e}")
        token = None
    
    # Test 4: Access protected endpoint
    if token:
        print("\n4. Testing protected endpoint...")
        try:
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(f"{BASE_URL}/auth/me", headers=headers)
            print(f"   Status: {response.status_code}")
            print(f"   Response: {response.json()}")
            if response.status_code == 200:
                print("   ✅ Protected endpoint accessible")
            else:
                print("   ❌ Protected endpoint failed")
        except Exception as e:
            print(f"   Error: {e}")
    
    # Test 5: Access patients endpoint (requires auth)
    if token:
        print("\n5. Testing patients endpoint...")
        try:
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.get(f"{BASE_URL}/patients", headers=headers)
            print(f"   Status: {response.status_code}")
            print(f"   Response: {response.json()}")
            if response.status_code == 200:
                print("   ✅ Patients endpoint accessible")
            else:
                print("   ❌ Patients endpoint failed")
        except Exception as e:
            print(f"   Error: {e}")
    
    # Test 6: Test without authentication
    print("\n6. Testing without authentication...")
    try:
        response = requests.get(f"{BASE_URL}/patients")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.json()}")
        if response.status_code == 401:
            print("   ✅ Authentication properly required")
        else:
            print("   ❌ Authentication not enforced")
    except Exception as e:
        print(f"   Error: {e}")
    
    # Test 7: Logout
    if token:
        print("\n7. Testing logout...")
        try:
            headers = {"Authorization": f"Bearer {token}"}
            response = requests.post(f"{BASE_URL}/auth/logout", headers=headers)
            print(f"   Status: {response.status_code}")
            print(f"   Response: {response.json()}")
            if response.status_code == 200:
                print("   ✅ Logout successful")
            else:
                print("   ❌ Logout failed")
        except Exception as e:
            print(f"   Error: {e}")
    
    # Test 8: Test admin login
    print("\n8. Testing admin login...")
    try:
        admin_data = {
            "username": "admin",
            "password": "Admin123!"
        }
        response = requests.post(f"{BASE_URL}/auth/login", json=admin_data)
        print(f"   Status: {response.status_code}")
        result = response.json()
        print(f"   Response: {result}")
        
        if response.status_code == 200:
            print("   ✅ Admin login successful")
            admin_token = result.get("token")
            admin_user = result.get("user")
            print(f"   Admin role: {admin_user.get('role')}")
            
            # Test admin endpoint
            if admin_token:
                print("\n9. Testing admin endpoint...")
                headers = {"Authorization": f"Bearer {admin_token}"}
                response = requests.get(f"{BASE_URL}/admin/users", headers=headers)
                print(f"   Status: {response.status_code}")
                print(f"   Response: {response.json()}")
                if response.status_code == 200:
                    print("   ✅ Admin endpoint accessible")
                else:
                    print("   ❌ Admin endpoint failed")
        else:
            print("   ❌ Admin login failed")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n" + "=" * 50)
    print("🏁 Authentication system test completed!")

if __name__ == "__main__":
    test_auth_system() 