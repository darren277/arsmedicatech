""""""
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
def handle_options(path):
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
def stream_events():
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

    def event_stream():
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
def sse():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    # Example event data
    event_data = {
        "type": "new_message",
        "conversation_id": "test-123",
        "sender": "Test User",
        "text": "This is a test message",
        "timestamp": str(time.time())
    }
    publish_event_with_buffer(user_id, event_data)

    return jsonify({"message": "Event published successfully"}), 200

@app.route('/api/test/appointment-reminder', methods=['POST'])
def test_appointment_reminder():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    event_data = {
        "type": "appointment_reminder",
        "appointmentId": data.get('appointmentId', 'test-123'),
        "time": data.get('time', str(time.time())),
        "content": data.get('content', 'Test appointment reminder'),
        "timestamp": str(time.time())
    }
    publish_event_with_buffer(user_id, event_data)

    return jsonify({"message": "Appointment reminder sent successfully"}), 200



@app.route('/api/', methods=['GET'])
def hello_world():
    return jsonify({"data": "Hello World"})

# Authentication endpoints
@app.route('/api/auth/register', methods=['POST'])
def register():
    return register_route()

@app.route('/api/auth/login', methods=['POST'])
def login():
    return login_route()

@app.route('/api/auth/logout', methods=['POST'])
@require_auth
def logout():
    return logout_route()

@app.route('/api/auth/me', methods=['GET'])
@require_auth
def get_current_user_info():
    return get_current_user_info_route()

@app.route('/api/auth/change-password', methods=['POST'])
@require_auth
def change_password():
    return change_password_route()

# Admin endpoints
@app.route('/api/admin/users', methods=['GET'])
@require_admin
def get_all_users():
    return get_all_users_route()

@app.route('/api/admin/users/<user_id>/deactivate', methods=['POST'])
@require_admin
def deactivate_user(user_id):
    return deactivate_user_route(user_id)

@app.route('/api/admin/users/<user_id>/activate', methods=['POST'])
@require_admin
def activate_user(user_id):
    return activate_user_route(user_id)

@app.route('/api/admin/setup', methods=['POST'])
def setup_default_admin():
    return setup_default_admin_route()

@app.route('/api/users/exist', methods=['GET'])
def check_users_exist():
    return check_users_exist_route()

@app.route('/api/debug/session', methods=['GET'])
def debug_session():
    return debug_session_route()

@app.route('/api/users/search', methods=['GET'])
@require_auth
def search_users():
    return search_users_route()

@app.route('/api/conversations', methods=['GET'])
@require_auth
def get_user_conversations():
    return get_user_conversations_route()

@app.route('/api/conversations/<conversation_id>/messages', methods=['GET'])
@require_auth
def get_conversation_messages(conversation_id):
    return get_conversation_messages_route(conversation_id)

@app.route('/api/conversations/<conversation_id>/messages', methods=['POST'])
@require_auth
def send_message(conversation_id):
    return send_message_route(conversation_id)

@app.route('/api/conversations', methods=['POST'])
@require_auth
def create_conversation():
    return create_conversation_route()

@app.route('/api/chat', methods=['GET', 'POST'])
@optional_auth
def chat_endpoint():
    if request.method == 'GET':
        return jsonify(DUMMY_CONVERSATIONS)
    elif request.method == 'POST':
        data = request.json
        # In a real app, you'd save this to a database
        # For now, we'll just return success
        return jsonify({"message": "Conversations saved successfully"})

@app.route('/api/llm_chat', methods=['GET', 'POST'])
@optional_auth
def llm_agent_endpoint():
    return llm_agent_endpoint_route()

@app.route('/api/llm_chat/reset', methods=['POST'])
@optional_auth
def reset_llm_chat():
    """Reset the LLM chat session"""
    session.pop('agent_data', None)
    return jsonify({"message": "Chat session reset successfully"})

@app.route('/api/time')
#@cross_origin()
def get_current_time():
    response = jsonify({'time': time.time()})
    return response

@app.route('/api/patients', methods=['GET', 'POST'])
def patients_endpoint():
    return patients_endpoint_route()

@app.route('/api/patients/<patient_id>', methods=['GET', 'PUT', 'DELETE'])
def patient_endpoint(patient_id):
    return patient_endpoint_route(patient_id)

@app.route('/api/patients/search', methods=['GET'])
@require_auth
def search_patients():
    return search_patients_route()

# Encounter endpoints
@app.route('/api/encounters', methods=['GET'])
@require_auth
def get_all_encounters():
    return get_all_encounters_route()

@app.route('/api/encounters/search', methods=['GET'])
@require_auth
def search_encounters():
    return search_encounters_route()

@app.route('/api/patients/<patient_id>/encounters', methods=['GET'])
@require_auth
def get_patient_encounters(patient_id):
    return get_encounters_by_patient_route(patient_id)

@app.route('/api/encounters/<encounter_id>', methods=['GET'])
@require_auth
def get_encounter(encounter_id):
    return get_encounter_by_id_route(encounter_id)

@app.route('/api/patients/<patient_id>/encounters', methods=['POST'])
@require_auth
def create_patient_encounter(patient_id):
    return create_encounter_route(patient_id)

@app.route('/api/encounters/<encounter_id>', methods=['PUT'])
@require_auth
def update_encounter(encounter_id):
    return update_encounter_route(encounter_id)

@app.route('/api/encounters/<encounter_id>', methods=['DELETE'])
@require_auth
def delete_encounter(encounter_id):
    return delete_encounter_route(encounter_id)

@app.route('/api/test_surrealdb', methods=['GET'])
@require_admin
def test_surrealdb():
    return test_surrealdb_route()

@app.route('/api/test_crud', methods=['GET'])
def test_crud():
    """Test endpoint to verify CRUD operations"""
    return test_crud_route()

@app.route('/api/intake/<patient_id>', methods=['PATCH'])
def patch_intake(patient_id):
    return patch_intake_route(patient_id)

@app.route('/api/settings', methods=['GET', 'POST'])
@require_auth
def settings():
    return settings_route()

@app.route('/api/usage', methods=['GET'])
@require_auth
def api_usage():
    return get_api_usage_route()

@app.route('/api/profile', methods=['GET'])
@require_auth
def get_user_profile():
    return get_user_profile_route()

@app.route('/api/profile', methods=['POST'])
@require_auth
def update_user_profile():
    return update_user_profile_route()

# Appointment endpoints
@app.route('/api/appointments', methods=['GET'])
@require_auth
def get_appointments():
    return get_appointments_route()

@app.route('/api/appointments', methods=['POST'])
@require_auth
def create_appointment():
    return create_appointment_route()

@app.route('/api/appointments/<appointment_id>', methods=['GET'])
@require_auth
def get_appointment(appointment_id):
    return get_appointment_route(appointment_id)

@app.route('/api/appointments/<appointment_id>', methods=['PUT'])
@require_auth
def update_appointment(appointment_id):
    return update_appointment_route(appointment_id)

@app.route('/api/appointments/<appointment_id>/cancel', methods=['POST'])
@require_auth
def cancel_appointment(appointment_id):
    return cancel_appointment_route(appointment_id)

@app.route('/api/appointments/<appointment_id>/confirm', methods=['POST'])
@require_auth
def confirm_appointment(appointment_id):
    return confirm_appointment_route(appointment_id)

@app.route('/api/appointments/available-slots', methods=['GET'])
@require_auth
def get_available_slots():
    return get_available_slots_route()

@app.route('/api/appointments/types', methods=['GET'])
@require_auth
def get_appointment_types():
    return get_appointment_types_route()

@app.route('/api/appointments/statuses', methods=['GET'])
@require_auth
def get_appointment_statuses():
    return get_appointment_statuses_route()


# Register the SSE blueprint
app.register_blueprint(sse_bp)

from asgiref.wsgi import WsgiToAsgi

asgi_app = WsgiToAsgi(app)

if __name__ == '__main__': app.run(port=PORT, debug=DEBUG, host=HOST)

