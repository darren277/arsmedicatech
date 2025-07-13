#!/usr/bin/env python3
"""
Webhook System Test Script

This script tests the complete webhook functionality:
1. Creates webhook subscriptions
2. Creates appointments to trigger webhooks
3. Monitors webhook delivery
"""
import json
import time
import requests
from datetime import datetime, timedelta
from typing import Dict, Any


class WebhookTester:
    def __init__(self, base_url: str = "http://localhost:5000"):
        self.base_url = base_url
        self.session = requests.Session()
        self.user_id = None
        self.subscriptions = []
        
    def login(self, username: str = "admin", password: str = "admin") -> bool:
        """Login to get session cookie"""
        try:
            response = self.session.post(
                f"{self.base_url}/api/auth/login",
                json={"username": username, "password": password}
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ Login successful: {data.get('message', 'Logged in')}")
                return True
            else:
                print(f"❌ Login failed: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Login error: {e}")
            return False
    
    def create_webhook_subscription(self, event_name: str, target_url: str, secret: str = "test-secret") -> Dict[str, Any]:
        """Create a webhook subscription"""
        try:
            data = {
                "event_name": event_name,
                "target_url": target_url,
                "secret": secret,
                "enabled": True
            }
            
            response = self.session.post(
                f"{self.base_url}/api/webhooks",
                json=data
            )
            
            if response.status_code == 201:
                result = response.json()
                subscription = result.get('subscription', {})
                self.subscriptions.append(subscription)
                print(f"✅ Created webhook subscription for {event_name}: {subscription.get('id')}")
                return subscription
            else:
                print(f"❌ Failed to create webhook subscription: {response.status_code} - {response.text}")
                return {}
                
        except Exception as e:
            print(f"❌ Error creating webhook subscription: {e}")
            return {}
    
    def get_webhook_subscriptions(self) -> list:
        """Get all webhook subscriptions"""
        try:
            response = self.session.get(f"{self.base_url}/api/webhooks")
            
            if response.status_code == 200:
                data = response.json()
                subscriptions = data.get('subscriptions', [])
                print(f"📋 Found {len(subscriptions)} webhook subscriptions")
                return subscriptions
            else:
                print(f"❌ Failed to get webhook subscriptions: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"❌ Error getting webhook subscriptions: {e}")
            return []
    
    def create_appointment(self, patient_id: str = "patient:test123", provider_id: str = "provider:test456") -> Dict[str, Any]:
        """Create an appointment to trigger webhooks"""
        try:
            # Create appointment for tomorrow
            tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
            
            data = {
                "patient_id": patient_id,
                "provider_id": provider_id,
                "appointment_date": tomorrow,
                "start_time": "10:00",
                "end_time": "10:30",
                "appointment_type": "consultation",
                "notes": "Test appointment for webhook testing",
                "location": "Test Clinic"
            }
            
            response = self.session.post(
                f"{self.base_url}/api/appointments",
                json=data
            )
            
            if response.status_code == 201:
                result = response.json()
                appointment = result.get('appointment', {})
                print(f"✅ Created appointment: {appointment.get('id')}")
                return appointment
            else:
                print(f"❌ Failed to create appointment: {response.status_code} - {response.text}")
                return {}
                
        except Exception as e:
            print(f"❌ Error creating appointment: {e}")
            return {}
    
    def update_appointment(self, appointment_id: str) -> bool:
        """Update an appointment to trigger update webhook"""
        try:
            data = {
                "notes": "Updated notes for webhook testing",
                "location": "Updated Test Clinic"
            }
            
            response = self.session.put(
                f"{self.base_url}/api/appointments/{appointment_id}",
                json=data
            )
            
            if response.status_code == 200:
                print(f"✅ Updated appointment: {appointment_id}")
                return True
            else:
                print(f"❌ Failed to update appointment: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Error updating appointment: {e}")
            return False
    
    def cancel_appointment(self, appointment_id: str) -> bool:
        """Cancel an appointment to trigger cancellation webhook"""
        try:
            data = {"reason": "Test cancellation for webhook testing"}
            
            response = self.session.post(
                f"{self.base_url}/api/appointments/{appointment_id}/cancel",
                json=data
            )
            
            if response.status_code == 200:
                print(f"✅ Cancelled appointment: {appointment_id}")
                return True
            else:
                print(f"❌ Failed to cancel appointment: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Error cancelling appointment: {e}")
            return False
    
    def confirm_appointment(self, appointment_id: str) -> bool:
        """Confirm an appointment to trigger confirmation webhook"""
        try:
            response = self.session.post(
                f"{self.base_url}/api/appointments/{appointment_id}/confirm"
            )
            
            if response.status_code == 200:
                print(f"✅ Confirmed appointment: {appointment_id}")
                return True
            else:
                print(f"❌ Failed to confirm appointment: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Error confirming appointment: {e}")
            return False
    
    def get_available_events(self) -> list:
        """Get available webhook events"""
        try:
            response = self.session.get(f"{self.base_url}/api/webhooks/events")
            
            if response.status_code == 200:
                data = response.json()
                events = data.get('events', [])
                print(f"📋 Available webhook events:")
                for event in events:
                    print(f"  - {event['value']}: {event['description']}")
                return events
            else:
                print(f"❌ Failed to get events: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"❌ Error getting events: {e}")
            return []
    
    def run_full_test(self, webhook_url: str = "https://webhook.site/your-unique-url"):
        """Run a complete webhook test"""
        print("🚀 Starting Webhook System Test")
        print("=" * 50)
        
        # Step 1: Login
        if not self.login():
            print("❌ Cannot proceed without login")
            return
        
        # Step 2: Get available events
        self.get_available_events()
        print()
        
        # Step 3: Create webhook subscriptions for all events
        events = [
            "appointment.created",
            "appointment.updated", 
            "appointment.cancelled",
            "appointment.confirmed",
            "appointment.completed"
        ]
        
        for event in events:
            self.create_webhook_subscription(event, webhook_url)
            time.sleep(0.5)  # Small delay between requests
        
        print()
        
        # Step 4: List all subscriptions
        self.get_webhook_subscriptions()
        print()
        
        # Step 5: Create an appointment (triggers appointment.created)
        print("📅 Creating appointment to trigger webhooks...")
        appointment = self.create_appointment()
        
        if not appointment:
            print("❌ Cannot proceed without creating appointment")
            return
        
        appointment_id = appointment.get('id')
        print(f"⏳ Waiting 3 seconds for webhook delivery...")
        time.sleep(3)
        
        # Step 6: Update the appointment (triggers appointment.updated)
        print("📝 Updating appointment...")
        self.update_appointment(appointment_id)
        print(f"⏳ Waiting 3 seconds for webhook delivery...")
        time.sleep(3)
        
        # Step 7: Confirm the appointment (triggers appointment.confirmed)
        print("✅ Confirming appointment...")
        self.confirm_appointment(appointment_id)
        print(f"⏳ Waiting 3 seconds for webhook delivery...")
        time.sleep(3)
        
        # Step 8: Cancel the appointment (triggers appointment.cancelled)
        print("❌ Cancelling appointment...")
        self.cancel_appointment(appointment_id)
        print(f"⏳ Waiting 3 seconds for webhook delivery...")
        time.sleep(3)
        
        print()
        print("🎉 Webhook test completed!")
        print("=" * 50)
        print("📋 Check your webhook endpoint to see the delivered webhooks:")
        print(f"   {webhook_url}")
        print()
        print("📊 Expected webhooks:")
        print("   1. appointment.created")
        print("   2. appointment.updated") 
        print("   3. appointment.confirmed")
        print("   4. appointment.cancelled")


def main():
    """Main test function"""
    print("🔧 Webhook System Test Script")
    print("=" * 50)
    
    # Get webhook URL from user
    webhook_url = input("Enter your webhook URL (or press Enter for webhook.site): ").strip()
    
    if not webhook_url:
        print("🌐 Please go to https://webhook.site and copy your unique URL")
        webhook_url = input("Enter your webhook.site URL: ").strip()
        
        if not webhook_url:
            print("❌ No webhook URL provided. Exiting.")
            return
    
    # Create tester and run test
    tester = WebhookTester()
    tester.run_full_test(webhook_url)


if __name__ == "__main__":
    main()
