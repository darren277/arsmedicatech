import hashlib
import secrets
import re
from datetime import datetime, timedelta
from typing import Optional, Dict, Any


class User:
    def __init__(self, username: str, email: str, password: str = None, 
                 first_name: str = None, last_name: str = None, 
                 role: str = "user", is_active: bool = True, 
                 created_at: str = None, id: str = None):
        """
        Initialize a User object
        
        :param username: Unique username
        :param email: User's email address
        :param password: Plain text password (will be hashed)
        :param first_name: User's first name
        :param last_name: User's last name
        :param role: User role (user, admin, doctor, nurse)
        :param is_active: Whether the user account is active
        :param created_at: Creation timestamp
        :param id: Database record ID
        """
        self.username = username
        self.email = email
        self.first_name = first_name or ""
        self.last_name = last_name or ""
        self.role = role
        self.is_active = is_active
        self.created_at = created_at or datetime.utcnow().isoformat()
        self.id = id
        
        # Hash password if provided
        if password:
            self.password_hash = self._hash_password(password)
        else:
            self.password_hash = None
    
    def _hash_password(self, password: str) -> str:
        """Hash a password using SHA-256 with salt"""
        salt = secrets.token_hex(16)
        hash_obj = hashlib.sha256()
        hash_obj.update((password + salt).encode('utf-8'))
        return f"{salt}${hash_obj.hexdigest()}"
    
    def verify_password(self, password: str) -> bool:
        """Verify a password against the stored hash"""
        if not self.password_hash:
            print(f"[DEBUG] No password hash stored for user")
            return False
        
        try:
            print(f"[DEBUG] Stored password hash: {self.password_hash}")
            print(f"[DEBUG] Attempting to verify password: {password}")
            salt, hash_value = self.password_hash.split('$', 1)
            print(f"[DEBUG] Extracted salt: {salt}")
            print(f"[DEBUG] Extracted hash: {hash_value}")
            
            hash_obj = hashlib.sha256()
            hash_obj.update((password + salt).encode('utf-8'))
            computed_hash = hash_obj.hexdigest()
            print(f"[DEBUG] Computed hash: {computed_hash}")
            print(f"[DEBUG] Hash match: {computed_hash == hash_value}")
            
            return computed_hash == hash_value
        except (ValueError, AttributeError) as e:
            print(f"[DEBUG] Password verification error: {e}")
            return False
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert user to dictionary for database storage"""
        return {
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'role': self.role,
            'is_active': self.is_active,
            'created_at': self.created_at,
            'password_hash': self.password_hash
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'User':
        """Create user from dictionary"""
        # Convert RecordID to string if it exists
        user_id = data.get('id')
        if hasattr(user_id, '__str__'):
            user_id = str(user_id)
        
        user = cls(
            username=data.get('username'),
            email=data.get('email'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            role=data.get('role', 'user'),
            is_active=data.get('is_active', True),
            created_at=data.get('created_at'),
            id=user_id
        )
        # Set password hash if it exists in the data
        if 'password_hash' in data:
            user.password_hash = data['password_hash']
        return user
    
    @staticmethod
    def validate_username(username: str) -> tuple[bool, str]:
        """Validate username format"""
        if not username:
            return False, "Username is required"
        if len(username) < 3:
            return False, "Username must be at least 3 characters long"
        if len(username) > 30:
            return False, "Username must be less than 30 characters"
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            return False, "Username can only contain letters, numbers, and underscores"
        return True, ""
    
    @staticmethod
    def validate_email(email: str) -> tuple[bool, str]:
        """Validate email format"""
        if not email:
            return False, "Email is required"
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            return False, "Invalid email format"
        return True, ""
    
    @staticmethod
    def validate_password(password: str) -> tuple[bool, str]:
        """Validate password strength"""
        if not password:
            return False, "Password is required"
        if len(password) < 8:
            return False, "Password must be at least 8 characters long"
        if not re.search(r'[A-Z]', password):
            return False, "Password must contain at least one uppercase letter"
        if not re.search(r'[a-z]', password):
            return False, "Password must contain at least one lowercase letter"
        if not re.search(r'\d', password):
            return False, "Password must contain at least one number"
        return True, ""
    
    def get_full_name(self) -> str:
        """Get user's full name"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return self.username
    
    def has_role(self, required_role: str) -> bool:
        """Check if user has the required role"""
        role_hierarchy = {
            'user': 1,
            'nurse': 2,
            'doctor': 3,
            'admin': 4
        }
        
        user_level = role_hierarchy.get(self.role, 0)
        required_level = role_hierarchy.get(required_role, 0)
        
        return user_level >= required_level
    
    def is_admin(self) -> bool:
        """Check if user is an admin"""
        return self.role == 'admin'
    
    def is_doctor(self) -> bool:
        """Check if user is a doctor or admin"""
        return self.has_role('doctor')
    
    def is_nurse(self) -> bool:
        """Check if user is a nurse, doctor, or admin"""
        return self.has_role('nurse')


class UserSession:
    """Manages user sessions and authentication tokens"""
    
    def __init__(self, user_id: str, username: str, role: str, 
                 created_at: str = None, expires_at: str = None):
        self.user_id = user_id
        self.username = username
        self.role = role
        self.created_at = created_at or datetime.utcnow().isoformat()
        self.expires_at = expires_at or (datetime.utcnow() + timedelta(hours=24)).isoformat()
        self.token = secrets.token_urlsafe(32)
    
    def is_expired(self) -> bool:
        """Check if session has expired"""
        try:
            expires = datetime.fromisoformat(self.expires_at)
            return datetime.utcnow() > expires
        except (ValueError, TypeError):
            return True
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert session to dictionary"""
        return {
            'user_id': self.user_id,
            'username': self.username,
            'role': self.role,
            'created_at': self.created_at,
            'expires_at': self.expires_at,
            'token': self.token
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UserSession':
        """Create session from dictionary"""
        session = cls(
            user_id=data.get('user_id'),
            username=data.get('username'),
            role=data.get('role'),
            created_at=data.get('created_at'),
            expires_at=data.get('expires_at')
        )
        # Set the token from the data if it exists
        if 'token' in data:
            session.token = data['token']
        return session
