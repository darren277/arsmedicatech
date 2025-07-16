"""
Optimal table route.
"""

from typing import Tuple

from flask import Response, jsonify, request

from lib.opt.hypertension import main
from lib.services.optimal import OptimalService
from lib.services.user_service import UserService
from lib.services.auth_decorators import get_current_user_id
from settings import OPTIMAL_URL, logger


def call_optimal_route() -> Tuple[Response, int]:
    """
    Uses the Optimal Service to call the Optimal API to perform a mathematical optimization.
    :return: Response object with optimal table data.
    """
    try:
        # Get current user ID
        user_id = get_current_user_id()
        if not user_id:
            return jsonify({"error": "Authentication required"}), 401
        
        # Get user's Optimal API key
        user_service = UserService()
        user_service.connect()
        try:
            api_key = user_service.get_optimal_api_key(user_id)
            if not api_key:
                return jsonify({"error": "Optimal API key not configured. Please add your Optimal API key in Settings."}), 400
        finally:
            user_service.close()
        
        # Get table data from request
        data = request.get_json()
        if not data or 'tableData' not in data:
            return jsonify({"error": "Table data is required"}), 400
        
        table_data = data['tableData']
        
        # Create hypertension optimization schema
        hypertension_schema = main()
        
        # Create Optimal service instance with user's API key
        service = OptimalService(
            url=OPTIMAL_URL,
            api_key=api_key,
            schema=hypertension_schema
        )
        
        # Send optimization request
        result = service.send()
        
        logger.info(f"Optimal service call successful: {result}")
        
        return jsonify({
            "message": "Optimal table processed successfully",
            "result": result,
            "tableData": table_data
        }), 200
        
    except Exception as e:
        logger.error(f"Error calling Optimal service: {str(e)}")
        return jsonify({"error": f"Failed to process optimal table: {str(e)}"}), 500
