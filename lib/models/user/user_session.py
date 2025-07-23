"""
User Session model.
"""
import secrets
from datetime import datetime, timedelta, timezone
from typing import Any, Dict, Optional


class UserSession:
    """
    Manages user sessions and authentication tokens
    """
    
    def __init__(
            self,
            user_id: str,
            username: str,
            role: str,
            created_at: Optional[str] = None,
            expires_at: Optional[str] = None
    ) -> None:
        """
        Initialize a UserSession object
        :param user_id: Unique user ID
        :param username: User's username
        :param role: User's role (patient, provider, admin)
        :param created_at: Creation timestamp (ISO format)
        :param expires_at: Expiration timestamp (ISO format, defaults to 24 hours from now)
        :raises ValueError: If user_id or username is empty
        :raises ValueError: If role is not one of the valid roles
        :raises ValueError: If created_at or expires_at is not in ISO format
        :raises ValueError: If expires_at is before created_at
        :raises ValueError: If token generation fails
        :return: None
        """
        if not user_id or not username:
            raise ValueError("user_id and username cannot be empty")
        if role not in ['patient', 'provider', 'admin']:
            raise ValueError("Role must be one of: patient, provider, admin")

        self.user_id = user_id
        self.username = username
        self.role = role

        if created_at:
            try:
                datetime.fromisoformat(created_at)
            except ValueError:
                raise ValueError("created_at must be in ISO format")

        if expires_at:
            try:
                expires = datetime.fromisoformat(expires_at)
                if expires < datetime.fromisoformat(created_at or datetime.now(timezone.utc).isoformat()):
                    raise ValueError("expires_at must be after created_at")
            except ValueError:
                raise ValueError("expires_at must be in ISO format")
        else:
            expires_at = (datetime.now(timezone.utc) + timedelta(hours=24)).isoformat()

        self.created_at = created_at or datetime.now(timezone.utc).isoformat()
        self.expires_at = expires_at or (datetime.now(timezone.utc) + timedelta(hours=24)).isoformat()

        try:
            self.token = secrets.token_urlsafe(32)
        except Exception as e:
            raise ValueError(f"Failed to generate token: {e}")
    
    def is_expired(self) -> bool:
        """
        Check if session has expired

        :return: True if session is expired, False otherwise
        """
        try:
            expires = datetime.fromisoformat(self.expires_at)
            return datetime.now(timezone.utc) > expires
        except (ValueError, TypeError):
            return True
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert session to dictionary

        :return: Dictionary representation of the session
        """
        return {
            'user_id': self.user_id,
            'username': self.username,
            'role': self.role,
            'created_at': self.created_at,
            'expires_at': self.expires_at,
            'session_token': self.session_token
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UserSession':
        """
        Create session from dictionary

        :param data: Dictionary containing session data
        :return: UserSession object
        """
        session = cls(
            user_id=str(data.get('user_id', '')),
            username=str(data.get('username', '')),
            role=str(data.get('role', 'patient')),
            created_at=data.get('created_at'),
            expires_at=data.get('expires_at')
        )
        # Set the token from the data if it exists
        if 'session_token' in data:
            session.token = data['session_token']
        return session
