"""
OpenAI Security Service
"""
import time
from typing import Any, Dict, Optional, Tuple

from openai import AuthenticationError, OpenAI, RateLimitError

from lib.services.user_service import UserService
from settings import logger


class OpenAISecurityService:
    """
    Service for managing OpenAI API security, validation, and rate limiting
    """
    
    def __init__(self) -> None:
        """
        Initialize the OpenAI security service
        """
        self.rate_limit_cache: Dict[str, Dict[str, Any]] = {}
        self.api_key_cache: Dict[str, Dict[str, Any]] = {}
        self.rate_limit_window = 3600  # 1 hour
        self.max_requests_per_hour = 100  # Adjust based on your needs
    
    def validate_api_key(self, api_key: str) -> Tuple[bool, str]:
        """
        Validate an OpenAI API key by making a test request
        
        :param api_key: The API key to validate
        :return: (is_valid, error_message)
        """
        if not api_key or not api_key.startswith('sk-'):
            return False, "Invalid API key format"
        
        try:
            client = OpenAI(api_key=api_key)
            # Make a minimal test request to validate the key
            logger.debug("About to validate API key")
            response = client.models.list()
            logger.debug(f"OpenAI API key validation response: {response}")
            return True, ""
        except AuthenticationError:
            return False, "Invalid API key"
        except RateLimitError:
            return False, "API key rate limit exceeded"
        except Exception as e:
            return False, f"API key validation failed: {str(e)}"
    
    def check_rate_limit(self, user_id: str) -> Tuple[bool, str]:
        """
        Check if user has exceeded rate limits
        
        :param user_id: User ID to check
        :return: (within_limit, error_message)
        """
        current_time = time.time()
        user_key = f"rate_limit:{user_id}"
        
        if user_key not in self.rate_limit_cache:
            self.rate_limit_cache[user_key] = {
                'requests': 0,
                'window_start': current_time
            }
        
        user_data = self.rate_limit_cache[user_key]
        
        # Reset window if expired
        if current_time - user_data['window_start'] > self.rate_limit_window:
            user_data['requests'] = 0
            user_data['window_start'] = current_time
        
        # Check if limit exceeded
        if user_data['requests'] >= self.max_requests_per_hour:
            return False, "Rate limit exceeded. Please try again later."
        
        # Increment request count
        user_data['requests'] += 1
        return True, ""
    
    def get_user_api_key_with_validation(self, user_id: str) -> Tuple[Optional[str], str]:
        """
        Get user's API key with validation and rate limiting
        
        :param user_id: User ID
        :return: (api_key, error_message)
        """
        # Check rate limit first
        within_limit, rate_error = self.check_rate_limit(user_id)
        if not within_limit:
            return None, rate_error
        
        # Get API key from user service
        user_service = UserService()
        user_service.connect()
        try:
            api_key = user_service.get_openai_api_key(user_id)
            if not api_key:
                return None, "OpenAI API key not configured. Please add your API key in Settings."
            
            # Validate API key (with caching to avoid repeated validation)
            cache_key = f"validation:{user_id}"
            current_time = time.time()
            
            if cache_key in self.api_key_cache:
                cached_data = self.api_key_cache[cache_key]
                # Cache validation for 1 hour
                if current_time - cached_data['timestamp'] < 3600:
                    if cached_data['is_valid']:
                        return api_key, ""
                    else:
                        return None, cached_data['error']
            
            # Validate API key
            is_valid, error = self.validate_api_key(api_key)
            
            # Cache result
            self.api_key_cache[cache_key] = {
                'is_valid': is_valid,
                'error': error,
                'timestamp': current_time
            }
            
            if is_valid:
                return api_key, ""
            else:
                return None, f"API key validation failed: {error}"
                
        finally:
            user_service.close()
    
    def log_api_usage(self, user_id: str, model: str, tokens_used: int = 0) -> None:
        """
        Log API usage for monitoring and billing
        
        :param user_id: User ID
        :param model: Model used
        :param tokens_used: Number of tokens used
        :return: None
        """
        # TODO: Implement usage logging to database
        logger.debug(f"[USAGE] User {user_id} used {model} with {tokens_used} tokens")

    def get_usage_stats(self, user_id: str) -> Dict[str, Any]:
        """
        Get usage statistics for a user
        
        :param user_id: User ID
        :return: Usage statistics
        """
        user_key = f"rate_limit:{user_id}"
        if user_key in self.rate_limit_cache:
            user_data = self.rate_limit_cache[user_key]
            return {
                'requests_this_hour': user_data['requests'],
                'max_requests_per_hour': self.max_requests_per_hour,
                'window_start': user_data['window_start']
            }
        return {
            'requests_this_hour': 0,
            'max_requests_per_hour': self.max_requests_per_hour,
            'window_start': time.time()
        }


# Global security service instance
_openai_security_service = None


def get_openai_security_service() -> OpenAISecurityService:
    """
    Get the global OpenAI security service instance
    :return: OpenAISecurityService instance
    """
    global _openai_security_service
    if _openai_security_service is None:
        _openai_security_service = OpenAISecurityService()
    return _openai_security_service 