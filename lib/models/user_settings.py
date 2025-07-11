from datetime import datetime
from typing import Dict, Any, Optional
from lib.services.encryption import get_encryption_service

from settings import logger


class UserSettings:
    """Model for user settings and preferences"""
    
    def __init__(self, user_id: str, openai_api_key: str = None, 
                 created_at: str = None, updated_at: str = None, id: str = None):
        """
        Initialize user settings
        
        :param user_id: ID of the user these settings belong to
        :param openai_api_key: OpenAI API key (will be encrypted)
        :param created_at: Creation timestamp
        :param updated_at: Last update timestamp
        :param id: Database record ID
        """
        self.user_id = user_id
        self.openai_api_key = openai_api_key
        self.created_at = created_at or datetime.utcnow().isoformat()
        self.updated_at = updated_at or datetime.utcnow().isoformat()
        self.id = id
    
    def set_openai_api_key(self, api_key: str):
        """Set OpenAI API key (will be encrypted)"""
        self.openai_api_key = api_key
        self.updated_at = datetime.utcnow().isoformat()
    
    def get_openai_api_key(self) -> str:
        """Get decrypted OpenAI API key"""
        if not self.openai_api_key:
            logger.debug("No API key stored in settings")
            return ""
        
        logger.debug(f"Attempting to decrypt API key (stored length: {len(self.openai_api_key)})")
        try:
            encryption_service = get_encryption_service()
            result = encryption_service.decrypt_api_key(self.openai_api_key)
            logger.debug(f"API key decryption result length: {len(result)}")
            return result
        except Exception as e:
            logger.error(f"Failed to decrypt OpenAI API key: {e}")
            return ""
    
    def has_openai_api_key(self) -> bool:
        """Check if user has a valid OpenAI API key"""
        return bool(self.get_openai_api_key())
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert settings to dictionary for database storage"""
        # Encrypt API key before storing
        encrypted_api_key = ""
        if self.openai_api_key:
            try:
                encryption_service = get_encryption_service()
                encrypted_api_key = encryption_service.encrypt_api_key(self.openai_api_key)
            except Exception as e:
                logger.error(f"Failed to encrypt OpenAI API key: {e}")
        
        return {
            'user_id': self.user_id,
            'openai_api_key': encrypted_api_key,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'UserSettings':
        """Create settings from dictionary"""
        # Convert RecordID to string if it exists
        settings_id = data.get('id')
        if hasattr(settings_id, '__str__'):
            settings_id = str(settings_id)
        
        settings = cls(
            user_id=data.get('user_id'),
            created_at=data.get('created_at'),
            updated_at=data.get('updated_at'),
            id=settings_id
        )
        
        # Store encrypted API key as-is (will be decrypted when accessed)
        if 'openai_api_key' in data:
            settings.openai_api_key = data['openai_api_key']
        
        return settings
    
    @staticmethod
    def validate_openai_api_key(api_key: str) -> tuple[bool, str]:
        """Validate OpenAI API key format"""
        if not api_key:
            return False, "OpenAI API key is required"
        
        # Basic validation - OpenAI API keys start with 'sk-' and are 51 characters long
        if not api_key.startswith('sk-'):
            return False, "OpenAI API key must start with 'sk-'"
        
        if len(api_key) != 51:
            return False, "OpenAI API key must be 51 characters long"
        
        return True, "" 