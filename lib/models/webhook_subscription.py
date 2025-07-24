"""
Webhook subscription model for storing webhook configurations
"""
from datetime import datetime, timezone
from typing import Any, Dict, Optional, Union


class WebhookSubscription:
    """
    Model representing a webhook subscription.
    """
    
    def __init__(
            self,
            event_name: str,
            target_url: str,
            secret: str,
            enabled: bool = True,
            id: Optional[str] = None,
            created_at: Optional[Union[str, datetime]] = None,
            updated_at: Optional[Union[str, datetime]] = None
    ) -> None:
        """
        Initialize a WebhookSubscription object
        
        :param event_name: Name of the event to subscribe to (e.g., 'appointment.created')
        :param target_url: URL where webhook should be sent
        :param secret: Secret key for HMAC signature
        :param enabled: Whether the subscription is active
        :param id: Database record ID
        :param created_at: Creation timestamp
        :param updated_at: Last update timestamp
        """
        if not event_name or not target_url or not secret:
            raise ValueError("Missing required fields: event_name, target_url, secret")
        
        self.event_name = event_name
        self.target_url = target_url
        self.secret = secret
        self.enabled = enabled
        self.id = id
        self.created_at = created_at or datetime.now(timezone.utc).isoformat()
        self.updated_at = updated_at or datetime.now(timezone.utc).isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert webhook subscription to dictionary for database storage
        
        :return: Dictionary representation of the webhook subscription
        """
        # Convert ISO strings to datetime objects for SurrealDB
        created_at = self.created_at
        updated_at = self.updated_at
        
        # If they're strings, convert to datetime objects
        if isinstance(created_at, str):
            try:
                created_at = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
            except (ValueError, AttributeError):
                pass
                
        if isinstance(updated_at, str):
            try:
                updated_at = datetime.fromisoformat(updated_at.replace('Z', '+00:00'))
            except (ValueError, AttributeError):
                pass
        
        return {
            'event_name': self.event_name,
            'target_url': self.target_url,
            'secret': self.secret,
            'enabled': self.enabled,
            'created_at': created_at,
            'updated_at': updated_at
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "WebhookSubscription":
        print(f"[from_dict] Called with data: {data}")
        try:
            # Handle id as RecordID or string
            id_val = data.get("id")
            if id_val is not None and not isinstance(id_val, str):
                id_val = str(id_val)
            # Handle datetimes as ISO strings
            created_at = data.get("created_at")
            if isinstance(created_at, datetime):
                created_at = created_at.isoformat()
            updated_at = data.get("updated_at")
            if isinstance(updated_at, datetime):
                updated_at = updated_at.isoformat()
            return cls(
                event_name=data["event_name"],
                target_url=data["target_url"],
                secret=data["secret"],
                enabled=data.get("enabled", True),
                id=id_val,
                created_at=created_at,
                updated_at=updated_at,
            )
        except Exception as e:
            import traceback
            print(f"[WebhookSubscription.from_dict] Error parsing: {data}\nException: {e}")
            traceback.print_exc()
            raise 