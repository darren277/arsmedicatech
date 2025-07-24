"""
Redis client for connecting to a Redis database.
"""
import redis

from settings import REDIS_HOST, REDIS_PORT, NOTIFICATIONS_CHANNEL


def get_redis_connection()-> redis.Redis:
    """
    Creates a Redis client connection.
    :return: redis.Redis
    """
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=NOTIFICATIONS_CHANNEL, decode_responses=True)
