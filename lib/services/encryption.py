import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from typing import Optional


class EncryptionService:
    """Service for encrypting and decrypting sensitive data like API keys"""
    
    def __init__(self, master_key: Optional[str] = None):
        """
        Initialize encryption service
        
        :param master_key: Master key for encryption. If not provided, will use environment variable ENCRYPTION_KEY
        """
        if master_key:
            self.master_key = master_key
        else:
            # Get from environment variable
            self.master_key = os.getenv('ENCRYPTION_KEY')
            if not self.master_key:
                raise ValueError("ENCRYPTION_KEY environment variable must be set")
        
        # Generate a key from the master key using PBKDF2
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'arsmedicatech_salt',  # Fixed salt for consistency
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.master_key.encode()))
        self.cipher = Fernet(key)
    
    def encrypt(self, data: str) -> str:
        """
        Encrypt a string
        
        :param data: String to encrypt
        :return: Base64 encoded encrypted string
        """
        if not data:
            return ""
        
        encrypted_data = self.cipher.encrypt(data.encode())
        return base64.urlsafe_b64encode(encrypted_data).decode()
    
    def decrypt(self, encrypted_data: str) -> str:
        """
        Decrypt a string
        
        :param encrypted_data: Base64 encoded encrypted string
        :return: Decrypted string
        """
        if not encrypted_data:
            return ""
        
        try:
            encrypted_bytes = base64.urlsafe_b64decode(encrypted_data.encode())
            decrypted_data = self.cipher.decrypt(encrypted_bytes)
            return decrypted_data.decode()
        except Exception as e:
            print(f"[ERROR] Failed to decrypt data: {e}")
            return ""
    
    def encrypt_api_key(self, api_key: str) -> str:
        """
        Encrypt an API key with additional security
        
        :param api_key: API key to encrypt
        :return: Encrypted API key
        """
        if not api_key:
            return ""
        
        # Add a prefix to identify this as an API key
        prefixed_data = f"API_KEY:{api_key}"
        return self.encrypt(prefixed_data)
    
    def decrypt_api_key(self, encrypted_api_key: str) -> str:
        """
        Decrypt an API key
        
        :param encrypted_api_key: Encrypted API key
        :return: Decrypted API key
        """
        if not encrypted_api_key:
            return ""
        
        decrypted_data = self.decrypt(encrypted_api_key)
        if decrypted_data.startswith("API_KEY:"):
            return decrypted_data[8:]  # Remove prefix
        return decrypted_data


# Global encryption service instance
_encryption_service = None


def get_encryption_service() -> EncryptionService:
    """Get the global encryption service instance"""
    global _encryption_service
    if _encryption_service is None:
        _encryption_service = EncryptionService()
    return _encryption_service
