"""
Optimal table route.
"""

from typing import Tuple

from flask import Response, jsonify, request

from lib.opt.hypertension import main
from lib.services.optimal import OptimalService
from settings import OPTIMAL_KEY, OPTIMAL_URL, logger


def call_optimal_route() -> Tuple[Response, int]:
    """
    Uses the Optimal Service to call the Optimal API to perform a mathematical optimization.
    :return: Response object with optimal table data.
    """
    try:
        # Get table data from request
        data = request.get_json()
        if not data or 'tableData' not in data:
            return jsonify({"error": "Table data is required"}), 400
        
        table_data = data['tableData']
        
        # Create hypertension optimization schema
        hypertension_schema = main()
        
        # Create Optimal service instance
        service = OptimalService(
            url=OPTIMAL_URL,
            api_key=OPTIMAL_KEY,
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
