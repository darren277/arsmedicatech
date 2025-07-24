"""
Test script for the new profile functionality
"""

import json
import os
import sys

import requests

# Add the parent directory to the path so we can import from lib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_URL = "http://localhost:5000/api"

def test_profile_functionality():
    """Test the complete profile functionality"""
    print("🧪 Testing Profile Functionality")
    
    # Test user credentials
    test_user = {
        "username": "profiletest",
        "email": "profiletest@example.com",
        "password": "TestPass123!",
        "first_name": "Profile",
        "last_name": "Test",
        "role": "provider"
    }
    
    session = requests.Session()
    
    try:
        # Test 1: Register new user
        print("\n1. Registering new user...")
        response = session.post(f"{BASE_URL}/auth/register", json=test_user)
        print(f"Status: {response.status_code}")
        if response.status_code == 201:
            print("✅ User registered successfully")
        else:
            print(f"❌ Registration failed: {response.text}")
            return False
        
        # Test 2: Login
        print("\n2. Logging in...")
        login_data = {
            "username": test_user["username"],
            "password": test_user["password"]
        }
        response = session.post(f"{BASE_URL}/auth/login", json=login_data)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print("✅ Login successful")
            login_response = response.json()
            print(f"User role: {login_response.get('user', {}).get('role')}")
        else:
            print(f"❌ Login failed: {response.text}")
            return False
        
        # Test 3: Get user profile
        print("\n3. Getting user profile...")
        response = session.get(f"{BASE_URL}/profile")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            profile = response.json()
            print("✅ Profile retrieved successfully")
            print(f"Username: {profile.get('profile', {}).get('username')}")
            print(f"Role: {profile.get('profile', {}).get('role')}")
            print(f"Email: {profile.get('profile', {}).get('email')}")
        else:
            print(f"❌ Failed to get profile: {response.text}")
            return False
        
        # Test 4: Update profile
        print("\n4. Updating profile...")
        profile_updates = {
            "first_name": "Updated",
            "last_name": "Profile",
            "phone": "+1-555-123-4567",
            "specialty": "Cardiology",
            "clinic_name": "Heart Care Clinic",
            "clinic_address": "123 Medical Center Dr, Healthcare City, HC 12345"
        }
        response = session.post(f"{BASE_URL}/profile", json=profile_updates)
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            print("✅ Profile updated successfully")
        else:
            print(f"❌ Failed to update profile: {response.text}")
            return False
        
        # Test 5: Get updated profile
        print("\n5. Getting updated profile...")
        response = session.get(f"{BASE_URL}/profile")
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            updated_profile = response.json()
            profile_data = updated_profile.get('profile', {})
            print("✅ Updated profile retrieved successfully")
            print(f"First Name: {profile_data.get('first_name')}")
            print(f"Last Name: {profile_data.get('last_name')}")
            print(f"Phone: {profile_data.get('phone')}")
            print(f"Specialty: {profile_data.get('specialty')}")
            print(f"Clinic Name: {profile_data.get('clinic_name')}")
            print(f"Clinic Address: {profile_data.get('clinic_address')}")
        else:
            print(f"❌ Failed to get updated profile: {response.text}")
            return False
        
        # Test 6: Test validation (invalid phone)
        print("\n6. Testing validation (invalid phone)...")
        invalid_updates = {
            "phone": "invalid-phone"
        }
        response = session.post(f"{BASE_URL}/profile", json=invalid_updates)
        print(f"Status: {response.status_code}")
        if response.status_code == 400:
            print("✅ Validation working correctly")
        else:
            print(f"❌ Validation failed: {response.text}")
            return False
        
        print("\n🎉 All profile tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Test failed with exception: {e}")
        return False

def test_patient_profile():
    """Test profile functionality for a patient user"""
    print("\n🧪 Testing Patient Profile Functionality")
    
    # Test patient user credentials
    test_patient = {
        "username": "patienttest",
        "email": "patienttest@example.com",
        "password": "TestPass123!",
        "first_name": "Patient",
        "last_name": "Test",
        "role": "patient"
    }
    
    session = requests.Session()
    
    try:
        # Register patient user
        print("\n1. Registering patient user...")
        response = session.post(f"{BASE_URL}/auth/register", json=test_patient)
        if response.status_code != 201:
            print(f"❌ Patient registration failed: {response.text}")
            return False
        
        # Login
        print("\n2. Logging in as patient...")
        login_data = {
            "username": test_patient["username"],
            "password": test_patient["password"]
        }
        response = session.post(f"{BASE_URL}/auth/login", json=login_data)
        if response.status_code != 200:
            print(f"❌ Patient login failed: {response.text}")
            return False
        
        # Get patient profile
        print("\n3. Getting patient profile...")
        response = session.get(f"{BASE_URL}/profile")
        if response.status_code == 200:
            profile = response.json()
            profile_data = profile.get('profile', {})
            print(f"✅ Patient profile retrieved")
            print(f"Role: {profile_data.get('role')}")
            print(f"Name: {profile_data.get('first_name')} {profile_data.get('last_name')}")
        else:
            print(f"❌ Failed to get patient profile: {response.text}")
            return False
        
        # Update patient profile (should not include provider fields)
        print("\n4. Updating patient profile...")
        patient_updates = {
            "first_name": "Updated",
            "last_name": "Patient",
            "phone": "+1-555-987-6543"
        }
        response = session.post(f"{BASE_URL}/profile", json=patient_updates)
        if response.status_code == 200:
            print("✅ Patient profile updated successfully")
        else:
            print(f"❌ Failed to update patient profile: {response.text}")
            return False
        
        print("\n🎉 All patient profile tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Patient test failed with exception: {e}")
        return False

if __name__ == "__main__":
    print("Starting Profile Functionality Tests")
    print("=" * 50)
    
    # Test provider profile
    success1 = test_profile_functionality()
    
    # Test patient profile
    success2 = test_patient_profile()
    
    if success1 and success2:
        print("\n🎉 All tests passed!")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed!")
        sys.exit(1) 