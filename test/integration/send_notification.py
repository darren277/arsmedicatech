#!/usr/bin/env python3
"""Simple script to send a single notification"""

import json
import time
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.services.notifications import publish_event_with_buffer

def send_notification(user_id: str, notification_type: str, message: str = None):
    """Send a single notification"""
    
    # Create event data
    if notification_type == "new_message":
        event_data = {
            "type": "new_message",
            "conversation_id": "test-conv-123",
            "sender": "CLI Test",
            "text": message or f"Test message from CLI at {time.strftime('%H:%M:%S')}",
            "timestamp": str(time.time())
        }
    elif notification_type == "appointment_reminder":
        event_data = {
            "type": "appointment_reminder",
            "appointmentId": "test-apt-456",
            "time": "2025-01-20T14:00:00Z",
            "content": message or f"Test appointment reminder from CLI at {time.strftime('%H:%M:%S')}",
            "timestamp": str(time.time())
        }
    elif notification_type == "system_notification":
        event_data = {
            "type": "system_notification",
            "content": message or f"Test system notification from CLI at {time.strftime('%H:%M:%S')}",
            "timestamp": str(time.time())
        }
    else:
        print(f"❌ Unknown notification type: {notification_type}")
        print("   Available types: new_message, appointment_reminder, system_notification")
        return False
    
    try:
        publish_event_with_buffer(user_id, event_data)
        print(f"✅ Sent {notification_type} notification to user {user_id}")
        print(f"   Message: {event_data.get('text', event_data.get('content', 'N/A'))}")
        return True
    except Exception as e:
        print(f"❌ Failed to send notification: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python send_notification.py <user_id> <notification_type> [message]")
        print("")
        print("Examples:")
        print("  python send_notification.py test-user-123 new_message")
        print("  python send_notification.py test-user-123 new_message 'Hello from CLI!'")
        print("  python send_notification.py test-user-123 appointment_reminder 'Your appointment is tomorrow'")
        print("  python send_notification.py test-user-123 system_notification 'System maintenance scheduled'")
        print("")
        print("Available notification types:")
        print("  - new_message")
        print("  - appointment_reminder")
        print("  - system_notification")
        sys.exit(1)
    
    user_id = sys.argv[1]
    notification_type = sys.argv[2]
    message = sys.argv[3] if len(sys.argv) > 3 else None
    
    send_notification(user_id, notification_type, message) 