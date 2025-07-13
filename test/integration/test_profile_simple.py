#!/usr/bin/env python3
"""
Simple test script to verify the profile endpoint
"""

import json
import os
import sys

import requests

# Add the parent directory to the path so we can import from lib
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_URL = "http://localhost:5000/api"

def test_profile_endpoint():
    """Test the profile endpoint directly"""
    print("🧪 Testing Profile Endpoint")
    
    # Test 1: Try to access profile without authentication
    print("\n1. Testing profile endpoint without authentication...")
    response = requests.get(f"{BASE_URL}/profile")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    
    # Test 2: Try to access profile with invalid token
    print("\n2. Testing profile endpoint with invalid token...")
    headers = {"Authorization": "Bearer invalid_token"}
    response = requests.get(f"{BASE_URL}/profile", headers=headers)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
    
    # Test 3: Check if server is running
    print("\n3. Testing if server is running...")
    try:
        response = requests.get(f"{BASE_URL}/time")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")
    except requests.exceptions.ConnectionError:
        print("❌ Server is not running or not accessible")
        return False
    
    return True

if __name__ == "__main__":
    test_profile_endpoint() 