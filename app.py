"""
Main application file for the Flask server.
"""
import json
import time
from flask import Flask, jsonify, request, session, Response, Blueprint
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics

from lib.dummy_data import DUMMY_CONVERSATIONS
from lib.routes.chat import create_conversation_route, send_message_route, get_conversation_messages_route, \
    get_user_conversations_route
from lib.routes.llm_agent import llm_agent_endpoint_route
from lib.routes.patients import patch_intake_route, search_patients_route, patient_endpoint_route, \
    patients_endpoint_route, get_all_encounters_route, get_encounters_by_patient_route, get_encounter_by_id_route, \
    create_encounter_route, update_encounter_route, delete_encounter_route, search_encounters_route
from lib.routes.testing import test_surrealdb_route, test_crud_route, debug_session_route
from lib.routes.users import search_users_route, check_users_exist_route, setup_default_admin_route, \
    activate_user_route, deactivate_user_route, get_all_users_route, change_password_route, get_current_user_info_route, \
    logout_route, register_route, login_route, settings_route, get_api_usage_route, get_user_profile_route, update_user_profile_route
from lib.routes.appointments import create_appointment_route, get_appointments_route, get_appointment_route, \
    update_appointment_route, cancel_appointment_route, confirm_appointment_route, get_available_slots_route, \
    get_appointment_types_route, get_appointment_statuses_route
from lib.services.auth_decorators import require_auth, require_admin, optional_auth
from lib.services.notifications import publish_event, publish_event_with_buffer
from lib.services.redis_client import get_redis_connection
from settings import PORT, DEBUG, HOST, FLASK_SECRET_KEY
#from flask_jwt_extended import jwt_required, get_jwt_identity

from settings import logger


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:3012", "http://127.0.0.1:3012", "https://demo.arsmedicatech.com"], "supports_credentials": True, "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"], "allow_headers": ["Content-Type", "Authorization"]}})

app.secret_key = FLASK_SECRET_KEY
app.config['SESSION_COOKIE_SECURE'] = False  # Allow HTTP in development
app.config['SESSION_COOKIE_HTTPONLY'] = False  # Allow JavaScript access
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # Allow cross-site requests

# Global OPTIONS handler for CORS preflight
@app.route('/', defaults={'path': ''}, methods=['OPTIONS'])
@app.route('/<path:path>', methods=['OPTIONS'])
def handle_options(path: str) -> Response:
    """
    Global OPTIONS handler to handle CORS preflight requests.
    :param path: The path for which the OPTIONS request is made.
    :return: Response object with CORS headers.
    """
    logger.debug(f"Global OPTIONS handler called for path: {path}")
    response = Response()
    origin = request.headers.get('Origin')
    logger.debug(f"Global OPTIONS Origin: {origin}")
    response.headers['Access-Control-Allow-Origin'] = origin or '*'
    response.headers['Access-Control-Allow-Credentials'] = 'false'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, Accept, Cache-Control'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Max-Age'] = '86400'
    logger.debug(f"Global OPTIONS response headers: {dict(response.headers)}")
    return response

metrics = PrometheusMetrics(app)

app.config['CORS_HEADERS'] = 'Content-Type'


sse_bp = Blueprint('sse', __name__)


@sse_bp.route('/api/events/stream')
@sse_bp.route('/api/events/stream', methods=['OPTIONS'])
#@jwt_required()
def stream_events() -> Response:
    """
    Server-Sent Events (SSE) endpoint to stream events to the client.
    :return: Response object with the event stream.
    """
    logger.debug(f"SSE endpoint called - Method: {request.method}")
    logger.debug(f"SSE endpoint - Origin: {request.headers.get('Origin')}")
    logger.debug(f"SSE endpoint - Headers: {dict(request.headers)}")
    logger.debug(f"SSE endpoint - Session: {dict(session)}")
    logger.debug(f"SSE endpoint - Session cookie: {request.cookies.get('session')}")
    logger.debug(f"SSE endpoint - All cookies: {dict(request.cookies)}")
    logger.debug(f"SSE endpoint - Request URL: {request.url}")
    logger.debug(f"SSE endpoint - Request args: {dict(request.args)}")
    
    # Handle preflight OPTIONS request
    if request.method == 'OPTIONS':
        logger.debug("SSE endpoint - Handling OPTIONS preflight request")
        response = Response()
        origin = request.headers.get('Origin')
        logger.debug(f"OPTIONS Origin: {origin}")
        # Always allow the origin for SSE
        response.headers['Access-Control-Allow-Origin'] = origin or '*'
        logger.debug(f"Setting Access-Control-Allow-Origin to: {origin or '*'}")
        response.headers['Access-Control-Allow-Credentials'] = 'false'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, Accept, Cache-Control'
        response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
        response.headers['Access-Control-Max-Age'] = '86400'
        logger.debug(f"OPTIONS response headers: {dict(response.headers)}")
        logger.debug("SSE endpoint - Returning OPTIONS response")
        return response

    user_id = session.get('user_id')
    logger.debug(f"SSE endpoint - user_id from session: {user_id}")

    # For testing, also try to get user_id from query parameter
    if not user_id:
        user_id = request.args.get('user_id')
        logger.debug(f"SSE endpoint - user_id from query param: {user_id}")

    if not user_id:
        logger.debug("SSE endpoint - No user_id in session or query param, returning 401")
        return Response("Unauthorized", status=401, mimetype="text/plain")

    redis = get_redis_connection()
    pubsub = redis.pubsub()
    pubsub.subscribe(f"user:{user_id}")

    # Optionally: get last known timestamp or event ID
    # For simplicity, we assume the frontend sends ?since=timestamp
    since = request.args.get('since')

    def event_stream() -> str:
        """
        Generator function to stream events to the client.
        :return: Yields event data as a string in SSE format.
        """
        # Replay missed events
        key = f"user:{user_id}:events"
        past_events = redis.lrange(key, 0, -1)

        for raw in past_events:
            try:
                event = json.loads(raw)
                if not since or event.get("timestamp") > since:
                    yield f"data: {json.dumps(event)}\n\n"
            except Exception as e:
                logger.error("Error parsing replay event:", e)

        for message in pubsub.listen():
            if message['type'] == 'message':
                yield f"data: {message['data']}\n\n"

    response = Response(event_stream(), mimetype="text/event-stream")
    # Allow both localhost and 127.0.0.1 for development
    origin = request.headers.get('Origin')
    logger.debug(f"GET Origin: {origin}")
    # Always allow the origin for SSE
    response.headers['Access-Control-Allow-Origin'] = origin or '*'
    logger.debug(f"Setting GET Access-Control-Allow-Origin to: {origin or '*'}")
    # Don't require credentials for SSE
    response.headers['Access-Control-Allow-Credentials'] = 'false'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, Accept, Cache-Control'
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['Connection'] = 'keep-alive'
    logger.debug(f"GET response headers: {dict(response.headers)}")
    return response


@app.route('/api/sse', methods=['GET'])
def sse() -> Response:
    """
    Test endpoint to publish an event to the SSE stream.
    :return: Response object indicating success or failure.
    """
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Unauthorized"}, 401)

    # Example event data
    event_data = {
        "type": "new_message",
        "conversation_id": "test-123",
        "sender": "Test User",
        "text": "This is a test message",
        "timestamp": str(time.time())
    }
    publish_event_with_buffer(user_id, event_data)

    return jsonify({"message": "Event published successfully"}, 200)

@app.route('/api/test/appointment-reminder', methods=['POST'])
def test_appointment_reminder() -> Response:
    """
    Test endpoint to send an appointment reminder event.
    :return: Response object indicating success or failure.
    """
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Unauthorized"}, 401)

    data = request.json
    event_data = {
        "type": "appointment_reminder",
        "appointmentId": data.get('appointmentId', 'test-123'),
        "time": data.get('time', str(time.time())),
        "content": data.get('content', 'Test appointment reminder'),
        "timestamp": str(time.time())
    }
    publish_event_with_buffer(user_id, event_data)

    return jsonify({"message": "Appointment reminder sent successfully"}, 200)



# Authentication endpoints
@app.route('/api/auth/register', methods=['POST'])
def register() -> Response:
    """
    Register a new user.
    :return: Response object with registration status.
    """
    return register_route()

@app.route('/api/auth/login', methods=['POST'])
def login() -> Response:
    """
    Login endpoint for users.
    :return: Response object with login status.
    """
    return login_route()

@app.route('/api/auth/logout', methods=['POST'])
@require_auth
def logout() -> Response:
    """
    Logout endpoint for users.
    :return: Response object with logout status.
    """
    return logout_route()

@app.route('/api/auth/me', methods=['GET'])
@require_auth
def get_current_user_info() -> Response:
    """
    Get the current user's information.
    :return: Response object with user information.
    """
    return get_current_user_info_route()

@app.route('/api/auth/change-password', methods=['POST'])
@require_auth
def change_password() -> Response:
    """
    Change the password for the current user.
    :return: Response object with change password status.
    """
    return change_password_route()

# Admin endpoints
@app.route('/api/admin/users', methods=['GET'])
@require_admin
def get_all_users() -> Response:
    """
    Get a list of all users.
    :return: Response object with user list.
    """
    return get_all_users_route()

@app.route('/api/admin/users/<user_id>/deactivate', methods=['POST'])
@require_admin
def deactivate_user(user_id: str) -> Response:
    """
    Deactivate a user by their user ID.
    :param user_id: The ID of the user to deactivate.
    :return: Response object with deactivation status.
    """
    return deactivate_user_route(user_id)

@app.route('/api/admin/users/<user_id>/activate', methods=['POST'])
@require_admin
def activate_user(user_id: str) -> Response:
    """
    Activate a user by their user ID.
    :param user_id: The ID of the user to activate.
    :return: Response object with activation status.
    """
    return activate_user_route(user_id)

@app.route('/api/admin/setup', methods=['POST'])
def setup_default_admin() -> Response:
    """
    Setup the default admin user and initial configuration.
    :return: Response object with setup status.
    """
    return setup_default_admin_route()

@app.route('/api/users/exist', methods=['GET'])
def check_users_exist() -> Response:
    """
    Check if users exist in the system.
    :return: Response object with existence check status.
    """
    return check_users_exist_route()

@app.route('/api/debug/session', methods=['GET'])
def debug_session() -> Response:
    """
    Debug endpoint to inspect the current session.
    :return: Response object with session data.
    """
    return debug_session_route()

@app.route('/api/users/search', methods=['GET'])
@require_auth
def search_users() -> Response:
    """
    Search for users in the system.
    :return: Response object with search results.
    """
    return search_users_route()

@app.route('/api/conversations', methods=['GET'])
@require_auth
def get_user_conversations() -> Response:
    """
    Get conversations for the authenticated user.
    :return: Response object with user conversations.
    """
    return get_user_conversations_route()

@app.route('/api/conversations/<conversation_id>/messages', methods=['GET'])
@require_auth
def get_conversation_messages(conversation_id: str) -> Response:
    """
    Get messages for a specific conversation.
    :param conversation_id: The ID of the conversation to retrieve messages for.
    :return: Response object with conversation messages.
    """
    return get_conversation_messages_route(conversation_id)

@app.route('/api/conversations/<conversation_id>/messages', methods=['POST'])
@require_auth
def send_message(conversation_id: str) -> Response:
    """
    Send a message to a specific conversation.
    :param conversation_id: The ID of the conversation to send a message to.
    :return: Response object with message sending status.
    """
    return send_message_route(conversation_id)

@app.route('/api/conversations', methods=['POST'])
@require_auth
def create_conversation() -> Response:
    """
    Create a new conversation for the authenticated user.
    :return: Response object with conversation creation status.
    """
    return create_conversation_route()

# TODO: Do we even use this one?
@app.route('/api/chat', methods=['GET', 'POST'])
@optional_auth
def chat_endpoint() -> Response:
    """
    Endpoint to handle chat conversations.
    :return: Response object with chat data.
    """
    if request.method == 'GET':
        return jsonify(DUMMY_CONVERSATIONS)
    elif request.method == 'POST':
        data = request.json
        # In a real app, you'd save this to a database
        # For now, we'll just return success
        return jsonify({"message": "Conversations saved successfully"})

@app.route('/api/llm_chat', methods=['GET', 'POST'])
@optional_auth
def llm_agent_endpoint() -> Response:
    """
    Endpoint for LLM agent interactions.
    :return: Response object with LLM agent data.
    """
    return llm_agent_endpoint_route()

@app.route('/api/llm_chat/reset', methods=['POST'])
@optional_auth
def reset_llm_chat() -> Response:
    """
    Reset the LLM chat session
    :return: Response object indicating the reset status.
    """
    session.pop('agent_data', None)
    return jsonify({"message": "Chat session reset successfully"})

@app.route('/api/time')
#@cross_origin()
def get_current_time() -> Response:
    """
    Endpoint to get the current server time.
    :return: Response object with the current time.
    """
    response = jsonify({'time': time.time()})
    return response

@app.route('/api/patients', methods=['GET', 'POST'])
def patients_endpoint() -> Response:
    """
    Endpoint to handle patient data.
    :return: Response object with patient data.
    """
    return patients_endpoint_route()

@app.route('/api/patients/<patient_id>', methods=['GET', 'PUT', 'DELETE'])
def patient_endpoint(patient_id: str) -> Response:
    """
    Endpoint to handle a specific patient by ID.
    :param patient_id: The ID of the patient to retrieve or modify.
    :return: Response object with patient data.
    """
    return patient_endpoint_route(patient_id)

@app.route('/api/patients/search', methods=['GET'])
@require_auth
def search_patients() -> Response:
    """
    Search for patients in the system.
    :return: Response object with search results.
    """
    return search_patients_route()

# Encounter endpoints
@app.route('/api/encounters', methods=['GET'])
@require_auth
def get_all_encounters() -> Response:
    """
    Get all encounters in the system.
    :return: Response object with all encounters.
    """
    return get_all_encounters_route()

@app.route('/api/encounters/search', methods=['GET'])
@require_auth
def search_encounters() -> Response:
    """
    Search for encounters in the system.
    :return: Response object with search results.
    """
    return search_encounters_route()

@app.route('/api/patients/<patient_id>/encounters', methods=['GET'])
@require_auth
def get_patient_encounters(patient_id: str) -> Response:
    """
    Get all encounters for a specific patient.
    :param patient_id: The ID of the patient to retrieve encounters for.
    :return: Response object with patient encounters.
    """
    return get_encounters_by_patient_route(patient_id)

@app.route('/api/encounters/<encounter_id>', methods=['GET'])
@require_auth
def get_encounter(encounter_id: str) -> Response:
    """
    Get a specific encounter by its ID.
    :param encounter_id: The ID of the encounter to retrieve.
    :return: Response object with encounter data.
    """
    return get_encounter_by_id_route(encounter_id)

@app.route('/api/patients/<patient_id>/encounters', methods=['POST'])
@require_auth
def create_patient_encounter(patient_id: str) -> Response:
    """
    Create a new encounter for a specific patient.
    :param patient_id: The ID of the patient to create an encounter for.
    :return: Response object with encounter creation status.
    """
    return create_encounter_route(patient_id)

@app.route('/api/encounters/<encounter_id>', methods=['PUT'])
@require_auth
def update_encounter(encounter_id: str) -> Response:
    """
    Update an existing encounter by its ID.
    :param encounter_id: The ID of the encounter to update.
    :return: Response object with encounter update status.
    """
    return update_encounter_route(encounter_id)

@app.route('/api/encounters/<encounter_id>', methods=['DELETE'])
@require_auth
def delete_encounter(encounter_id: str) -> Response:
    """
    Delete an existing encounter by its ID.
    :param encounter_id: The ID of the encounter to delete.
    :return: Response object with encounter deletion status.
    """
    return delete_encounter_route(encounter_id)

@app.route('/api/test_surrealdb', methods=['GET'])
@require_admin
def test_surrealdb() -> Response:
    """
    Test endpoint to verify SurrealDB connection
    :return: Response object with test status.
    """
    return test_surrealdb_route()

@app.route('/api/test_crud', methods=['GET'])
def test_crud() -> Response:
    """
    Test endpoint to verify CRUD operations
    :return: Response object with CRUD test status.
    """
    return test_crud_route()

@app.route('/api/intake/<patient_id>', methods=['PATCH'])
def patch_intake(patient_id: str) -> Response:
    """
    Patch the intake information for a specific patient.
    :param patient_id: The ID of the patient to patch intake information for.
    :return: Response object with intake patch status.
    """
    return patch_intake_route(patient_id)

@app.route('/api/settings', methods=['GET', 'POST'])
@require_auth
def settings() -> Response:
    """
    Endpoint to get or update user settings.
    :return: Response object with settings data or update status.
    """
    return settings_route()

@app.route('/api/usage', methods=['GET'])
@require_auth
def api_usage() -> Response:
    """
    Endpoint to get API usage statistics.
    :return: Response object with API usage data.
    """
    return get_api_usage_route()

@app.route('/api/profile', methods=['GET'])
@require_auth
def get_user_profile() -> Response:
    """
    Endpoint to get the user profile information.
    :return: Response object with user profile data.
    """
    return get_user_profile_route()

@app.route('/api/profile', methods=['POST'])
@require_auth
def update_user_profile() -> Response:
    """
    Endpoint to update the user profile information.
    :return: Response object with user profile update status.
    """
    return update_user_profile_route()

# Appointment endpoints
@app.route('/api/appointments', methods=['GET'])
@require_auth
def get_appointments() -> Response:
    """
    Get a list of appointments for the authenticated user.
    :return: Response object with appointments data.
    """
    return get_appointments_route()

@app.route('/api/appointments', methods=['POST'])
@require_auth
def create_appointment() -> Response:
    """
    Create a new appointment for the authenticated user.
    :return: Response object with appointment creation status.
    """
    return create_appointment_route()

@app.route('/api/appointments/<appointment_id>', methods=['GET'])
@require_auth
def get_appointment(appointment_id: str) -> Response:
    """
    Get details of a specific appointment by its ID.
    :param appointment_id: The ID of the appointment to retrieve.
    :return: Response object with appointment details.
    """
    return get_appointment_route(appointment_id)

@app.route('/api/appointments/<appointment_id>', methods=['PUT'])
@require_auth
def update_appointment(appointment_id: str) -> Response:
    """
    Update an existing appointment by its ID.
    :param appointment_id: The ID of the appointment to update.
    :return: Response object with appointment update status.
    """
    return update_appointment_route(appointment_id)

@app.route('/api/appointments/<appointment_id>/cancel', methods=['POST'])
@require_auth
def cancel_appointment(appointment_id: str) -> Response:
    """
    Cancel an existing appointment by its ID.
    :param appointment_id: The ID of the appointment to cancel.
    :return: Response object with appointment cancellation status.
    """
    return cancel_appointment_route(appointment_id)

@app.route('/api/appointments/<appointment_id>/confirm', methods=['POST'])
@require_auth
def confirm_appointment(appointment_id: str) -> Response:
    """
    Confirm an existing appointment by its ID.
    :param appointment_id: The ID of the appointment to confirm.
    :return: Response object with appointment confirmation status.
    """
    return confirm_appointment_route(appointment_id)

@app.route('/api/appointments/available-slots', methods=['GET'])
@require_auth
def get_available_slots() -> Response:
    """
    Get available time slots for appointments.
    :return: Response object with available slots data.
    """
    return get_available_slots_route()

@app.route('/api/appointments/types', methods=['GET'])
@require_auth
def get_appointment_types() -> Response:
    """
    Get a list of appointment types.
    :return: Response object with appointment types data.
    """
    return get_appointment_types_route()

@app.route('/api/appointments/statuses', methods=['GET'])
@require_auth
def get_appointment_statuses() -> Response:
    """
    Get a list of appointment statuses.
    :return: Response object with appointment statuses data.
    """
    return get_appointment_statuses_route()


# Register the SSE blueprint
app.register_blueprint(sse_bp)

from asgiref.wsgi import WsgiToAsgi

asgi_app = WsgiToAsgi(app)

if __name__ == '__main__': app.run(port=PORT, debug=DEBUG, host=HOST)

