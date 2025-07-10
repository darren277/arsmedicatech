from functools import wraps
from flask import request, jsonify, session
from typing import Optional
from lib.services.user_service import UserService
from lib.models.user import UserSession


def require_auth(f):
    """Decorator to require authentication for a route"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get token from request headers or session
        token = request.headers.get('Authorization')
        if token and token.startswith('Bearer '):
            token = token[7:]  # Remove 'Bearer ' prefix
            print(f"[DEBUG] Got Bearer token: {token[:10]}...")
        
        if not token:
            token = session.get('auth_token')
            print(f"[DEBUG] Got session token: {token[:10] if token else 'None'}...")
        
        if not token:
            print("[DEBUG] No token found")
            return jsonify({"error": "Authentication required"}), 401
        
        # Validate session
        user_service = UserService()
        user_service.connect()
        try:
            print(f"[DEBUG] Validating session token: {token[:10]}...")
            user_session = user_service.validate_session(token)
            if not user_session:
                print("[DEBUG] Session validation failed")
                return jsonify({"error": "Invalid or expired session"}), 401
            
            print(f"[DEBUG] Session validated for user: {user_session.username}")
            # Add user info to request context
            request.user_session = user_session
            request.user_id = user_session.user_id
            request.user_role = user_session.role
            
            return f(*args, **kwargs)
        finally:
            user_service.close()
    
    return decorated_function


def require_role(required_role: str):
    """Decorator to require a specific role for a route"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            # First check authentication
            auth_result = require_auth(lambda: None)()
            if auth_result is not None:
                return auth_result
            
            # Then check role
            user_session = getattr(request, 'user_session', None)
            if not user_session:
                return jsonify({"error": "Authentication required"}), 401
            
            # Check if user has required role
            user_service = UserService()
            user_service.connect()
            try:
                user = user_service.get_user_by_id(user_session.user_id)
                if not user or not user.has_role(required_role):
                    return jsonify({"error": f"Role '{required_role}' required"}), 403
                
                return f(*args, **kwargs)
            finally:
                user_service.close()
        
        return decorated_function
    return decorator


def require_admin(f):
    """Decorator to require admin role"""
    return require_role('admin')(f)


def require_provider(f):
    """Decorator to require provider role"""
    return require_role('provider')(f)


def require_patient(f):
    """Decorator to require patient role"""
    return require_role('patient')(f)


def optional_auth(f):
    """Decorator to optionally authenticate user (doesn't fail if no auth)"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Get token from request headers or session
        token = request.headers.get('Authorization')
        if token and token.startswith('Bearer '):
            token = token[7:]  # Remove 'Bearer ' prefix
        
        if not token:
            token = session.get('auth_token')
        
        if token:
            # Try to validate session
            user_service = UserService()
            user_service.connect()
            try:
                user_session = user_service.validate_session(token)
                if user_session:
                    # Add user info to request context
                    request.user_session = user_session
                    request.user_id = user_session.user_id
                    request.user_role = user_session.role
            finally:
                user_service.close()
        
        return f(*args, **kwargs)
    
    return decorated_function


def get_current_user() -> Optional[UserSession]:
    """Get current authenticated user session"""
    return getattr(request, 'user_session', None)


def get_current_user_id() -> Optional[str]:
    """Get current authenticated user ID"""
    return getattr(request, 'user_id', None)


def get_current_user_role() -> Optional[str]:
    """Get current authenticated user role"""
    return getattr(request, 'user_role', None) 