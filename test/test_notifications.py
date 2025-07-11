#!/usr/bin/env python3
"""Test script for sending notifications via Redis"""

import json
import time
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.services.redis_client import get_redis_connection
from lib.services.notifications import publish_event_with_buffer

def test_send_notification(user_id: str, notification_type: str = "new_message"):
    """Send a test notification to a specific user"""
    
    # Create test notification data based on type
    if notification_type == "new_message":
        event_data = {
            "type": "new_message",
            "conversation_id": "test-conv-123",
            "sender": "Test User",
            "text": f"Test message sent at {time.strftime('%H:%M:%S')}",
            "timestamp": str(time.time())
        }
    elif notification_type == "appointment_reminder":
        event_data = {
            "type": "appointment_reminder",
            "appointmentId": "test-apt-456",
            "time": "2025-01-20T14:00:00Z",
            "content": f"Test appointment reminder sent at {time.strftime('%H:%M:%S')}",
            "timestamp": str(time.time())
        }
    elif notification_type == "system_notification":
        event_data = {
            "type": "system_notification",
            "content": f"Test system notification sent at {time.strftime('%H:%M:%S')}",
            "timestamp": str(time.time())
        }
    else:
        print(f"Unknown notification type: {notification_type}")
        return False
    
    try:
        # Send the notification
        publish_event_with_buffer(user_id, event_data)
        print(f"✅ Sent {notification_type} notification to user {user_id}")
        print(f"   Message: {event_data.get('text', event_data.get('content', 'N/A'))}")
        return True
    except Exception as e:
        print(f"❌ Failed to send notification: {e}")
        return False

def test_redis_connection():
    """Test Redis connection"""
    try:
        redis = get_redis_connection()
        redis.ping()
        print("✅ Redis connection successful")
        return True
    except Exception as e:
        print(f"❌ Redis connection failed: {e}")
        return False

def list_user_events(user_id: str):
    """List all events for a user"""
    try:
        redis = get_redis_connection()
        key = f"user:{user_id}:events"
        events = redis.lrange(key, 0, -1)
        
        print(f"\n📋 Events for user {user_id}:")
        if not events:
            print("   No events found")
        else:
            for i, event_raw in enumerate(events):
                event = json.loads(event_raw)
                print(f"   {i+1}. {event.get('type')} - {event.get('text', event.get('content', 'N/A'))}")
        return True
    except Exception as e:
        print(f"❌ Failed to list events: {e}")
        return False

def main():
    print("🔔 Notification Testing Tool")
    print("=" * 40)
    
    # Test Redis connection first
    if not test_redis_connection():
        print("Cannot proceed without Redis connection")
        return
    
    # Get user ID from command line or use default
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
    else:
        user_id = input("Enter user ID to send notification to: ").strip()
        if not user_id:
            user_id = "test-user-123"
    
    print(f"\n🎯 Testing notifications for user: {user_id}")
    
    # Test different notification types
    notification_types = ["new_message", "appointment_reminder", "system_notification"]
    
    for notification_type in notification_types:
        print(f"\n📤 Sending {notification_type}...")
        test_send_notification(user_id, notification_type)
        time.sleep(1)  # Small delay between notifications
    
    # List all events for the user
    list_user_events(user_id)
    
    print(f"\n✅ Testing complete! Check your frontend for notifications.")
    print(f"   User ID: {user_id}")
    print(f"   Frontend should be running on: http://localhost:3012")

if __name__ == "__main__":
    main() 