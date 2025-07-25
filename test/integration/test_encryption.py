import os
import sys
import unittest

# Add the lib directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from services.encryption import EncryptionService


class TestEncryption(unittest.TestCase):
    def setUp(self):
        # Set a test encryption key
        os.environ['ENCRYPTION_KEY'] = 'test-encryption-key-for-testing-only'
        self.encryption_service = EncryptionService()
    
    def test_encrypt_decrypt(self):
        """Test basic encryption and decryption"""
        original_text = "Hello, World!"
        encrypted = self.encryption_service.encrypt(original_text)
        decrypted = self.encryption_service.decrypt(encrypted)
        
        self.assertEqual(original_text, decrypted)
        self.assertNotEqual(original_text, encrypted)
    
    def test_encrypt_decrypt_api_key(self):
        """Test API key specific encryption and decryption"""
        api_key = "sk-test123456789012345678901234567890123456789012345678901234567890"
        encrypted = self.encryption_service.encrypt_api_key(api_key)
        decrypted = self.encryption_service.decrypt_api_key(encrypted)
        
        self.assertEqual(api_key, decrypted)
        self.assertNotEqual(api_key, encrypted)
    
    def test_empty_strings(self):
        """Test handling of empty strings"""
        encrypted = self.encryption_service.encrypt("")
        decrypted = self.encryption_service.decrypt(encrypted)
        
        self.assertEqual("", decrypted)
    
    def test_api_key_validation(self):
        """Test API key validation"""
        from models.user_settings import UserSettings

        # Valid API key
        valid_key = "sk-test123456789012345678901234567890123456789012345678901234567890"
        valid, msg = UserSettings.validate_openai_api_key(valid_key)
        self.assertTrue(valid)
        self.assertEqual("", msg)
        
        # Invalid API key - wrong prefix
        invalid_key = "pk-test123456789012345678901234567890123456789012345678901234567890"
        valid, msg = UserSettings.validate_openai_api_key(invalid_key)
        self.assertFalse(valid)
        self.assertIn("must start with 'sk-'", msg)
        
        # Invalid API key - wrong length
        invalid_key = "sk-test123"
        valid, msg = UserSettings.validate_openai_api_key(invalid_key)
        self.assertFalse(valid)
        self.assertIn("must be 51 characters long", msg)
        
        # Empty API key
        valid, msg = UserSettings.validate_openai_api_key("")
        self.assertFalse(valid)
        self.assertIn("required", msg)


if __name__ == '__main__':
    unittest.main() 