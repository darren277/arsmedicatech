"""
Simple Webhook Test Script

This script provides a simple way to test the webhook system.
"""
import time
from datetime import datetime, timedelta

import requests

from settings import DEMO_ADMIN_PASSWORD, DEMO_ADMIN_USERNAME


def test_webhook_system():
    """Test the webhook system with a simple flow"""
    
    # Configuration
    base_url = "http://localhost:3123"
    webhook_url = input("Enter your webhook URL (e.g., http://localhost:8000/webhook): ").strip()
    
    if not webhook_url:
        #print("❌ No webhook URL provided. Exiting.")
        webhook_url = "http://localhost:8000/webhook"  # Default URL for testing
        #return
    
    # Create session
    session = requests.Session()
    
    print("🔧 Testing Webhook System")
    print("=" * 40)
    
    # Step 1: Login
    print("1. Logging in...")
    login_response = session.post(
        f"{base_url}/api/auth/login",
        json={"username": DEMO_ADMIN_USERNAME, "password": DEMO_ADMIN_PASSWORD}
    )
    
    if login_response.status_code != 200:
        print(f"❌ Login failed: {login_response.status_code}")
        return
    
    print("✅ Login successful")
    
    # Step 2: Create webhook subscription
    print("\n2. Creating webhook subscription...")
    subscription_data = {
        "event_name": "appointment.created",
        "target_url": webhook_url,
        "secret": "test-secret",
        "enabled": True
    }
    
    sub_response = session.post(
        f"{base_url}/api/webhooks",
        json=subscription_data
    )
    
    if sub_response.status_code == 201:
        print("✅ Webhook subscription created")
    else:
        print(f"❌ Failed to create subscription: {sub_response.status_code}")
        return
    
    # Step 3: Create appointment to trigger webhook
    print("\n3. Creating appointment...")
    tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
    
    appointment_data = {
        "patient_id": "patient:test123",
        "provider_id": "provider:test456",
        "appointment_date": tomorrow,
        "start_time": "10:00",
        "end_time": "10:30",
        "appointment_type": "consultation",
        "notes": "Test appointment for webhook",
        "location": "Test Clinic"
    }
    
    app_response = session.post(
        f"{base_url}/api/appointments",
        json=appointment_data
    )
    
    if app_response.status_code == 201:
        appointment = app_response.json().get('appointment', {})
        appointment_id = appointment.get('id')
        print(f"✅ Appointment created: {appointment_id}")
    else:
        print(f"❌ Failed to create appointment: {app_response.status_code}")
        return
    
    # Step 4: Wait and check for webhook
    print("\n4. Waiting for webhook delivery...")
    print("⏳ Check your webhook endpoint in 5 seconds...")
    time.sleep(5)
    
    print("\n🎉 Test completed!")
    print("=" * 40)
    print(f"📋 Check your webhook endpoint: {webhook_url}")
    print("📊 You should see a webhook with event: appointment.created")


if __name__ == "__main__":
    test_webhook_system()
