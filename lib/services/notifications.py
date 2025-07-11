""""""
import json

from lib.services.redis_client import get_redis_connection

def publish_event(user_id, event_data):
    redis = get_redis_connection()
    redis.publish(f"user:{user_id}", json.dumps(event_data))

def store_event(user_id, event_data):
    redis = get_redis_connection()
    key = f"user:{user_id}:events"
    redis.rpush(key, json.dumps(event_data))
    redis.expire(key, 60 * 60)  # Keep messages for 1 hour

def publish_event_with_buffer(user_id, event_data):
    redis = get_redis_connection()
    redis.publish(f"user:{user_id}", json.dumps(event_data))
    store_event(user_id, event_data)
