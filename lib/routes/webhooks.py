"""
Webhook routes for managing webhook subscriptions
"""
from typing import Any, Dict, List, Tuple

from flask import Response, jsonify, request

from lib.db.surreal import DbController
from lib.models.webhook_subscription import WebhookSubscription
from lib.services.auth_decorators import get_current_user
from settings import logger


def create_webhook_subscription_route() -> Tuple[Response, int]:
    """
    Create a new webhook subscription
    
    This endpoint allows users to create a new webhook subscription.
    It requires the user to be authenticated and provides necessary details
    such as event name, target URL, and secret for HMAC signing.
    
    Returns a JSON response with the subscription details if successful,
    or an error message if there was an issue.
    
    HTTP Status Codes:
    - 201 Created: Subscription successfully created
    - 400 Bad Request: Missing required fields or invalid data
    - 401 Unauthorized: User not authenticated
    - 500 Internal Server Error: An unexpected error occurred
    
    Example Request:
    POST /webhooks
    Content-Type: application/json
    {
        "event_name": "appointment.created",
        "target_url": "https://example.com/webhooks",
        "secret": "your-secret-key"
    }
    
    Example Response:
    HTTP/1.1 201 Created
    {
        "success": true,
        "message": "Webhook subscription created successfully",
        "subscription": {
            "id": "webhook_subscription:12345",
            "event_name": "appointment.created",
            "target_url": "https://example.com/webhooks",
            "enabled": true,
            "created_at": "2023-09-01T12:00:00Z"
        }
    }
    
    :return: JSON response with subscription details or error message
    """
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Get current user
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        # Extract subscription data
        event_name = data.get('event_name')
        target_url = data.get('target_url')
        secret = data.get('secret')
        enabled = data.get('enabled', True)
        
        # Validate required fields
        if not all([event_name, target_url, secret]):
            return jsonify({"error": "Missing required fields: event_name, target_url, secret"}), 400
        
        # Validate event name
        valid_events = [
            'appointment.created',
            'appointment.updated',
            'appointment.cancelled',
            'appointment.confirmed',
            'appointment.completed'
        ]
        if event_name not in valid_events:
            return jsonify({"error": f"Invalid event_name. Must be one of: {', '.join(valid_events)}"}), 400
        
        # Create subscription
        subscription = WebhookSubscription(
            event_name=event_name,
            target_url=target_url,
            secret=secret,
            enabled=enabled
        )
        
        # Save to database
        db = DbController()
        db.connect()
        try:
            result = db.create('webhook_subscription', subscription.to_dict())
            if result:
                subscription.id = result.get('id')
                
                return jsonify({
                    "success": True,
                    "message": "Webhook subscription created successfully",
                    "subscription": {
                        "id": subscription.id,
                        "event_name": subscription.event_name,
                        "target_url": subscription.target_url,
                        "enabled": subscription.enabled,
                        "created_at": subscription.created_at
                    }
                }), 201
            else:
                return jsonify({"error": "Failed to create webhook subscription"}), 500
                
        finally:
            db.close()
            
    except Exception as e:
        logger.error(f"Error creating webhook subscription: {e}")
        return jsonify({"error": "Internal server error"}), 500


def get_webhook_subscriptions_route() -> Tuple[Response, int]:
    """
    Get webhook subscriptions
    
    This endpoint retrieves all webhook subscriptions for the authenticated user.
    Returns a JSON response with the list of subscriptions.
    
    HTTP Status Codes:
    - 200 OK: Successfully retrieved subscriptions
    - 401 Unauthorized: User not authenticated
    - 500 Internal Server Error: An unexpected error occurred
    
    Example Request:
    GET /webhooks
    
    Example Response:
    HTTP/1.1 200 OK
    {
        "success": true,
        "subscriptions": [
            {
                "id": "webhook_subscription:12345",
                "event_name": "appointment.created",
                "target_url": "https://example.com/webhooks",
                "enabled": true,
                "created_at": "2023-09-01T12:00:00Z",
                "updated_at": "2023-09-01T12:00:00Z"
            }
        ],
        "total": 1
    }
    
    :return: JSON response with subscriptions or error message
    """
    try:
        # Get current user
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        # Get query parameters
        event_name = request.args.get('event_name')
        enabled = request.args.get('enabled')
        
        # Build query
        query = "SELECT * FROM webhook_subscription"
        params = {}
        
        if event_name:
            query += " WHERE event_name = $event_name"
            params["event_name"] = event_name
        
        if enabled is not None:
            if event_name:
                query += " AND enabled = $enabled"
            else:
                query += " WHERE enabled = $enabled"
            params["enabled"] = enabled.lower() == 'true'
        
        query += " ORDER BY created_at DESC"
        
        # Get subscriptions
        db = DbController()
        db.connect()
        try:
            results = db.query(query, params)
            subscriptions: List[Dict[str, Any]] = []
            
            for result in results:
                if result.get('result'):
                    for record in result['result']:
                        subscription = WebhookSubscription.from_dict(record)
                        subscriptions.append({
                            "id": subscription.id,
                            "event_name": subscription.event_name,
                            "target_url": subscription.target_url,
                            "enabled": subscription.enabled,
                            "created_at": subscription.created_at,
                            "updated_at": subscription.updated_at
                        })
            
            return jsonify({
                "success": True,
                "subscriptions": subscriptions,
                "total": len(subscriptions)
            }), 200
            
        finally:
            db.close()
            
    except Exception as e:
        logger.error(f"Error getting webhook subscriptions: {e}")
        return jsonify({"error": "Internal server error"}), 500


def get_webhook_subscription_route(subscription_id: str) -> Tuple[Response, int]:
    """
    Get a specific webhook subscription
    
    This endpoint retrieves details of a specific webhook subscription by its ID.
    Returns a JSON response with the subscription details or an error message.
    
    HTTP Status Codes:
    - 200 OK: Successfully retrieved subscription details
    - 401 Unauthorized: User not authenticated
    - 404 Not Found: Subscription not found
    - 500 Internal Server Error: An unexpected error occurred
    
    Example Request:
    GET /webhooks/webhook_subscription:12345
    
    Example Response:
    HTTP/1.1 200 OK
    {
        "success": true,
        "subscription": {
            "id": "webhook_subscription:12345",
            "event_name": "appointment.created",
            "target_url": "https://example.com/webhooks",
            "enabled": true,
            "created_at": "2023-09-01T12:00:00Z",
            "updated_at": "2023-09-01T12:00:00Z"
        }
    }
    
    :param subscription_id: The ID of the subscription to retrieve
    :return: JSON response with subscription details or error message
    """
    try:
        # Get current user
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        # Get subscription
        db = DbController()
        db.connect()
        try:
            query = "SELECT * FROM webhook_subscription WHERE id = $id"
            params = {"id": subscription_id}
            results = db.query(query, params)
            
            if results:
                for result in results:
                    if result.get('result'):
                        for record in result['result']:
                            subscription = WebhookSubscription.from_dict(record)
                            return jsonify({
                                "success": True,
                                "subscription": {
                                    "id": subscription.id,
                                    "event_name": subscription.event_name,
                                    "target_url": subscription.target_url,
                                    "enabled": subscription.enabled,
                                    "created_at": subscription.created_at,
                                    "updated_at": subscription.updated_at
                                }
                            }), 200
            
            return jsonify({"error": "Webhook subscription not found"}), 404
            
        finally:
            db.close()
            
    except Exception as e:
        logger.error(f"Error getting webhook subscription: {e}")
        return jsonify({"error": "Internal server error"}), 500


def update_webhook_subscription_route(subscription_id: str) -> Tuple[Response, int]:
    """
    Update a webhook subscription
    
    This endpoint allows users to update an existing webhook subscription.
    It requires the user to be authenticated and provides the subscription ID
    along with the fields to be updated.
    
    Returns a JSON response indicating success or failure of the update operation.
    
    HTTP Status Codes:
    - 200 OK: Subscription successfully updated
    - 400 Bad Request: Missing required fields or invalid data
    - 401 Unauthorized: User not authenticated
    - 404 Not Found: Subscription not found
    - 500 Internal Server Error: An unexpected error occurred
    
    Example Request:
    PUT /webhooks/webhook_subscription:12345
    Content-Type: application/json
    {
        "target_url": "https://new-example.com/webhooks",
        "enabled": false
    }
    
    Example Response:
    HTTP/1.1 200 OK
    {
        "success": true,
        "message": "Webhook subscription updated successfully"
    }
    
    :param subscription_id: The ID of the subscription to update
    :return: JSON response with success message or error details
    """
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Get current user
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        # Get current subscription
        db = DbController()
        db.connect()
        try:
            query = "SELECT * FROM webhook_subscription WHERE id = $id"
            params = {"id": subscription_id}
            results = db.query(query, params)
            
            if not results:
                return jsonify({"error": "Webhook subscription not found"}), 404
            
            subscription = None
            for result in results:
                if result.get('result'):
                    for record in result['result']:
                        subscription = WebhookSubscription.from_dict(record)
                        break
                    if subscription:
                        break
            
            if not subscription:
                return jsonify({"error": "Webhook subscription not found"}), 404
            
            # Update fields
            for key, value in data.items():
                if hasattr(subscription, key):
                    setattr(subscription, key, value)
            
            from datetime import datetime, timezone
            subscription.updated_at = datetime.now(timezone.utc)
            
            # Save to database
            result = db.update(subscription_id, subscription.to_dict())
            if result:
                return jsonify({
                    "success": True,
                    "message": "Webhook subscription updated successfully"
                }), 200
            else:
                return jsonify({"error": "Failed to update webhook subscription"}), 500
                
        finally:
            db.close()
            
    except Exception as e:
        logger.error(f"Error updating webhook subscription: {e}")
        return jsonify({"error": "Internal server error"}), 500


def delete_webhook_subscription_route(subscription_id: str) -> Tuple[Response, int]:
    """
    Delete a webhook subscription
    
    This endpoint allows users to delete an existing webhook subscription.
    It requires the user to be authenticated and provides the subscription ID.
    
    Returns a JSON response indicating success or failure of the deletion operation.
    
    HTTP Status Codes:
    - 200 OK: Subscription successfully deleted
    - 401 Unauthorized: User not authenticated
    - 404 Not Found: Subscription not found
    - 500 Internal Server Error: An unexpected error occurred
    
    Example Request:
    DELETE /webhooks/webhook_subscription:12345
    
    Example Response:
    HTTP/1.1 200 OK
    {
        "success": true,
        "message": "Webhook subscription deleted successfully"
    }
    
    :param subscription_id: The ID of the subscription to delete
    :return: JSON response with success message or error details
    """
    try:
        # Get current user
        current_user = get_current_user()
        if not current_user:
            return jsonify({"error": "Authentication required"}), 401
        
        # Delete subscription
        db = DbController()
        db.connect()
        try:
            result = db.delete(subscription_id)
            if result:
                return jsonify({
                    "success": True,
                    "message": "Webhook subscription deleted successfully"
                }), 200
            else:
                return jsonify({"error": "Webhook subscription not found"}), 404
                
        finally:
            db.close()
            
    except Exception as e:
        logger.error(f"Error deleting webhook subscription: {e}")
        return jsonify({"error": "Internal server error"}), 500


def get_webhook_events_route() -> Tuple[Response, int]:
    """
    Get available webhook events
    
    This endpoint retrieves a list of available webhook events.
    It can be used to populate dropdowns or selection lists in the UI.
    
    Returns a JSON response with the list of webhook events.
    
    HTTP Status Codes:
    - 200 OK: Successfully retrieved webhook events
    - 500 Internal Server Error: An unexpected error occurred
    
    Example Request:
    GET /webhooks/events
    
    Example Response:
    HTTP/1.1 200 OK
    {
        "success": true,
        "events": [
            {
                "value": "appointment.created",
                "label": "Appointment Created",
                "description": "Triggered when a new appointment is created"
            },
            {
                "value": "appointment.updated",
                "label": "Appointment Updated",
                "description": "Triggered when an appointment is updated"
            },
            {
                "value": "appointment.cancelled",
                "label": "Appointment Cancelled",
                "description": "Triggered when an appointment is cancelled"
            },
            {
                "value": "appointment.confirmed",
                "label": "Appointment Confirmed",
                "description": "Triggered when an appointment is confirmed"
            },
            {
                "value": "appointment.completed",
                "label": "Appointment Completed",
                "description": "Triggered when an appointment is marked as completed"
            }
        ]
    }
    
    :return: JSON response with webhook events or error message
    """
    try:
        events = [
            {
                "value": "appointment.created",
                "label": "Appointment Created",
                "description": "Triggered when a new appointment is created"
            },
            {
                "value": "appointment.updated",
                "label": "Appointment Updated",
                "description": "Triggered when an appointment is updated"
            },
            {
                "value": "appointment.cancelled",
                "label": "Appointment Cancelled",
                "description": "Triggered when an appointment is cancelled"
            },
            {
                "value": "appointment.confirmed",
                "label": "Appointment Confirmed",
                "description": "Triggered when an appointment is confirmed"
            },
            {
                "value": "appointment.completed",
                "label": "Appointment Completed",
                "description": "Triggered when an appointment is marked as completed"
            }
        ]
        
        return jsonify({
            "success": True,
            "events": events
        }), 200
        
    except Exception as e:
        logger.error(f"Error getting webhook events: {e}")
        return jsonify({"error": "Internal server error"}), 500 