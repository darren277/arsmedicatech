from flask import jsonify, request

from lib.services.auth_decorators import get_current_user_id, require_auth
from lib.services.user_service import UserService


def settings_route():
    """Handle settings requests"""
    if request.method == 'GET':
        return get_user_settings()
    elif request.method == 'POST':
        return update_user_settings()
    else:
        return jsonify({"error": "Method not allowed"}), 405


def get_user_settings():
    """Get current user's settings"""
    try:
        user_id = get_current_user_id()
        if not user_id:
            return jsonify({"error": "Authentication required"}), 401
        
        user_service = UserService()
        user_service.connect()
        try:
            settings = user_service.get_user_settings(user_id)
            if not settings:
                return jsonify({"error": "Failed to load settings"}), 500
            
            # Return settings without exposing the API key
            return jsonify({
                "success": True,
                "settings": {
                    "user_id": settings.user_id,
                    "has_openai_api_key": settings.has_openai_api_key(),
                    "created_at": settings.created_at,
                    "updated_at": settings.updated_at
                }
            })
        finally:
            user_service.close()
            
    except Exception as e:
        print(f"[ERROR] Error getting user settings: {e}")
        return jsonify({"error": "Internal server error"}), 500


def update_user_settings():
    """Update user settings"""
    try:
        user_id = get_current_user_id()
        if not user_id:
            return jsonify({"error": "Authentication required"}), 401
        
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        user_service = UserService()
        user_service.connect()
        try:
            # Handle OpenAI API key update
            if 'openai_api_key' in data:
                api_key = data['openai_api_key']
                success, message = user_service.update_openai_api_key(user_id, api_key)
                
                if success:
                    return jsonify({
                        "success": True,
                        "message": "OpenAI API key updated successfully"
                    })
                else:
                    return jsonify({"error": message}), 400
            
            return jsonify({"error": "No valid settings to update"}), 400
            
        finally:
            user_service.close()
            
    except Exception as e:
        print(f"[ERROR] Error updating user settings: {e}")
        return jsonify({"error": "Internal server error"}), 500
