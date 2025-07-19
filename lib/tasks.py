"""
Background tasks for webhook delivery
"""
import hmac
import hashlib
import json
import uuid
from datetime import datetime, timezone
from typing import Dict, Any

import requests

from lib.db.surreal import DbController
from lib.models.webhook_subscription import WebhookSubscription
from settings import logger


def _signature(secret: str, payload: bytes) -> str:
    """
    Generate HMAC signature for webhook payload
    
    :param secret: Secret key for signing
    :param payload: Payload bytes to sign
    :return: Hex digest of the signature
    """
    return hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()


def deliver_webhooks(event_name: str, payload: Dict[str, Any], max_retries: int = 5) -> None:
    """
    Deliver webhooks for a given event to all subscribed endpoints.
    
    This function runs in the background and handles retries, timeouts,
    and error handling for webhook delivery.
    
    :param event_name: Name of the event (e.g., 'appointment.created')
    :param payload: Event payload to send
    :param max_retries: Maximum number of retry attempts
    """
    db = DbController()
    try:
        db.connect()
        
        # Get all enabled subscriptions for this event
        query = "SELECT * FROM webhook_subscription WHERE event_name = $event_name AND enabled = true"
        params = {"event_name": event_name}
        results = db.query(query, params)
        
        subscriptions = []
        for result in results:
            try:
                subscriptions.append(WebhookSubscription.from_dict(result))
            except Exception as e:
                logger.error(f"Failed to parse webhook subscription: {e}")
                continue
        
        if not subscriptions:
            logger.debug(f"No webhook subscriptions found for event: {event_name}")
            return
        
        logger.info(f"Delivering webhook for event '{event_name}' to {len(subscriptions)} endpoints")
        
        # Prepare payload with metadata
        webhook_payload = {
            "event": event_name,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "delivery_id": str(uuid.uuid4()),
            "data": payload
        }
        
        body = json.dumps(webhook_payload).encode()
        
        # Deliver to each subscription
        for subscription in subscriptions:
            _deliver_to_subscription(subscription, body, webhook_payload, max_retries)
            
    except Exception as e:
        logger.error(f"Error in deliver_webhooks: {e}")
    finally:
        db.close()


def _deliver_to_subscription(
    subscription: WebhookSubscription, 
    body: bytes, 
    payload: Dict[str, Any], 
    max_retries: int
) -> None:
    """
    Deliver webhook to a specific subscription with retry logic
    
    :param subscription: Webhook subscription to deliver to
    :param body: Encoded payload body
    :param payload: Payload dictionary for logging
    :param max_retries: Maximum number of retry attempts
    """
    headers = {
        "Content-Type": "application/json",
        "X-Event-Type": payload["event"],
        "X-Delivery-Id": payload["delivery_id"],
        "X-Signature": _signature(subscription.secret, body),
        "User-Agent": "ArsMedicaTech-Webhooks/1.0"
    }
    
    for attempt in range(max_retries + 1):
        try:
            logger.debug(f"Attempting webhook delivery to {subscription.target_url} (attempt {attempt + 1})")
            
            response = requests.post(
                subscription.target_url,
                data=body,
                headers=headers,
                timeout=10
            )
            
            if response.status_code < 400:
                logger.info(f"Webhook delivered successfully to {subscription.target_url}")
                return
            else:
                logger.warning(
                    f"Webhook delivery failed to {subscription.target_url}: "
                    f"HTTP {response.status_code}"
                )
                
        except requests.exceptions.Timeout:
            logger.warning(f"Webhook delivery timeout to {subscription.target_url}")
        except requests.exceptions.ConnectionError:
            logger.warning(f"Webhook delivery connection error to {subscription.target_url}")
        except Exception as e:
            logger.error(f"Webhook delivery error to {subscription.target_url}: {e}")
        
        # If this wasn't the last attempt, wait before retrying
        if attempt < max_retries:
            wait_time = 2 ** attempt  # Exponential backoff: 1, 2, 4, 8, 16 seconds
            logger.debug(f"Retrying webhook delivery in {wait_time} seconds...")
            import time
            time.sleep(wait_time)
    
    logger.error(f"Webhook delivery failed to {subscription.target_url} after {max_retries + 1} attempts")
