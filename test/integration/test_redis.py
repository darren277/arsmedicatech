"""Test Redis connectivity and SSE functionality"""
import json
import time

from lib.services.notifications import publish_event, publish_event_with_buffer
from lib.services.redis_client import get_redis_connection


def test_redis_connection():
    """Test basic Redis connection"""
    try:
        redis = get_redis_connection()
        redis.ping()
        print("✅ Redis connection successful")
        return True
    except Exception as e:
        print(f"❌ Redis connection failed: {e}")
        return False

def test_publish_event():
    """Test publishing an event"""
    try:
        test_user_id = "test-user-123"
        event_data = {
            "type": "test_message",
            "message": "Hello from test!",
            "timestamp": str(time.time())
        }
        
        publish_event(test_user_id, event_data)
        print("✅ Event published successfully")
        return True
    except Exception as e:
        print(f"❌ Event publishing failed: {e}")
        return False

def test_publish_event_with_buffer():
    """Test publishing an event with buffer"""
    try:
        test_user_id = "test-user-456"
        event_data = {
            "type": "new_message",
            "conversation_id": "test-conv-123",
            "sender": "Test Sender",
            "text": "Test message with buffer",
            "timestamp": str(time.time())
        }
        
        publish_event_with_buffer(test_user_id, event_data)
        print("✅ Event with buffer published successfully")
        return True
    except Exception as e:
        print(f"❌ Event with buffer publishing failed: {e}")
        return False

def test_event_retrieval():
    """Test retrieving events from buffer"""
    try:
        test_user_id = "test-user-456"
        redis = get_redis_connection()
        key = f"user:{test_user_id}:events"
        
        events = redis.lrange(key, 0, -1)
        print(f"✅ Retrieved {len(events)} events from buffer")
        
        for i, event_raw in enumerate(events):
            event = json.loads(event_raw)
            print(f"  Event {i+1}: {event.get('type')} - {event.get('text', 'N/A')}")
        
        return True
    except Exception as e:
        print(f"❌ Event retrieval failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing Redis and SSE functionality...")
    print("=" * 50)
    
    # Test Redis connection
    if not test_redis_connection():
        print("❌ Cannot proceed without Redis connection")
        exit(1)
    
    # Test event publishing
    test_publish_event()
    test_publish_event_with_buffer()
    
    # Test event retrieval
    test_event_retrieval()
    
    print("=" * 50)
    print("✅ All tests completed!")
