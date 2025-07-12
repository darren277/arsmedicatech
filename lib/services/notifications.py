"""
Notifications Service
"""
import json

from lib.services.redis_client import get_redis_connection
from lib.data_types import UserID, EventData


def publish_event(user_id: UserID, event_data: EventData) -> None:
    """
    Publish an event to a user's Redis channel.
    :param user_id: UserID - The ID of the user to whom the event is being published.
    :param event_data: EventData - The data of the event to be published.
    :return: None
    """
    redis = get_redis_connection()
    redis.publish(f"user:{user_id}", json.dumps(event_data))

def store_event(user_id: UserID, event_data: EventData) -> None:
    """
    Store an event in Redis for a specific user.
    :param user_id: UserID - The ID of the user to whom the event is being stored.
    :param event_data: EventData - The data of the event to be stored.
    :return: None
    """
    redis = get_redis_connection()
    key = f"user:{user_id}:events"
    redis.rpush(key, json.dumps(event_data))
    redis.expire(key, 60 * 60)  # Keep messages for 1 hour

def publish_event_with_buffer(user_id: UserID, event_data: EventData) -> None:
    """
    Publish an event to a user's Redis channel and store it in a buffer.
    :param user_id: UserID - The ID of the user to whom the event is being published.
    :param event_data: EventData - The data of the event to be published and stored.
    :return: None
    """
    redis = get_redis_connection()
    redis.publish(f"user:{user_id}", json.dumps(event_data))
    store_event(user_id, event_data)
