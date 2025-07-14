"""
Main application file for the Flask server.
"""
import json
import time
from typing import Tuple, Union

import sentry_sdk
import werkzeug
from flask import (Blueprint, Flask, Response, jsonify, redirect, request,
                   session)
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics

from lib.dummy_data import DUMMY_CONVERSATIONS
from lib.event_handlers import register_event_handlers
from lib.routes.appointments import (cancel_appointment_route,
                                     confirm_appointment_route,
                                     create_appointment_route,
                                     get_appointment_route,
                                     get_appointment_statuses_route,
                                     get_appointment_types_route,
                                     get_appointments_route,
                                     get_available_slots_route,
                                     update_appointment_route)
from lib.routes.chat import (create_conversation_route,
                             get_conversation_messages_route,
                             get_user_conversations_route, send_message_route)
from lib.routes.llm_agent import llm_agent_endpoint_route
from lib.routes.organizations import get_organizations_route
from lib.routes.patients import (create_encounter_route,
                                 delete_encounter_route,
                                 get_all_encounters_route,
                                 get_encounter_by_id_route,
                                 get_encounters_by_patient_route,
                                 patch_intake_route, patient_endpoint_route,
                                 patients_endpoint_route,
                                 search_encounters_route,
                                 search_patients_route, update_encounter_route)
from lib.routes.testing import (debug_session_route, test_crud_route,
                                test_surrealdb_route)
from lib.routes.users import (activate_user_route, change_password_route,
                              check_users_exist_route, deactivate_user_route,
                              get_all_users_route, get_api_usage_route,
                              get_current_user_info_route,
                              get_user_profile_route, login_route,
                              logout_route, register_route, search_users_route,
                              settings_route, setup_default_admin_route,
                              update_user_profile_route)
from lib.routes.webhooks import (create_webhook_subscription_route,
                                 delete_webhook_subscription_route,
                                 get_webhook_events_route,
                                 get_webhook_subscription_route,
                                 get_webhook_subscriptions_route,
                                 update_webhook_subscription_route)
from lib.services.auth_decorators import (optional_auth, require_admin,
                                          require_auth)
from lib.services.lab_results import (LabResultsService,
                                      differential_hematology,
                                      general_chemistry, hematology,
                                      serum_proteins)
from lib.services.notifications import publish_event_with_buffer
from lib.services.redis_client import get_redis_connection
from settings import DEBUG, FLASK_SECRET_KEY, HOST, PORT, SENTRY_DSN, logger

#from flask_jwt_extended import jwt_required, get_jwt_identity


sentry_sdk.init(
    dsn=SENTRY_DSN,
    # Add data like request headers and IP for users,
    # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
    send_default_pii=True,
)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:3012", "http://127.0.0.1:3012", "https://demo.arsmedicatech.com"], "supports_credentials": True, "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"], "allow_headers": ["Content-Type", "Authorization"]}})

app.secret_key = FLASK_SECRET_KEY
app.config['SESSION_COOKIE_SECURE'] = False  # Allow HTTP in development
app.config['SESSION_COOKIE_HTTPONLY'] = False  # Allow JavaScript access
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # Allow cross-site requests

# Global OPTIONS handler for CORS preflight
@app.route('/', defaults={'path': ''}, methods=['OPTIONS'])
@app.route('/<path:path>', methods=['OPTIONS'])
def handle_options(path: str) -> Tuple[Response, int]:
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
def stream_events() -> Tuple[Response, int]:
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
def sse() -> Tuple[Response, int]:
    """
    Test endpoint to publish an event to the SSE stream.
    :return: Response object indicating success or failure.
    """
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
def test_appointment_reminder() -> Tuple[Response, int]:
    """
    Test endpoint to send an appointment reminder event.
    :return: Response object indicating success or failure.
    """
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



# Authentication endpoints
@app.route('/api/auth/register', methods=['POST'])
def register() -> Tuple[Response, int]:
    """
    Register a new user.
    :return: Response object with registration status.
    """
    return register_route()

@app.route('/api/auth/login', methods=['POST'])
def login() -> Tuple[Response, int]:
    """
    Login endpoint for users.
    :return: Response object with login status.
    """
    return login_route()

@app.route('/api/auth/logout', methods=['POST'])
@require_auth
def logout() -> Tuple[Response, int]:
    """
    Logout endpoint for users.
    :return: Response object with logout status.
    """
    return logout_route()

@app.route('/api/auth/me', methods=['GET'])
@require_auth
def get_current_user_info() -> Tuple[Response, int]:
    """
    Get the current user's information.
    :return: Response object with user information.
    """
    return get_current_user_info_route()

@app.route('/api/auth/change-password', methods=['POST'])
@require_auth
def change_password() -> Tuple[Response, int]:
    """
    Change the password for the current user.
    :return: Response object with change password status.
    """
    return change_password_route()

# Admin endpoints
@app.route('/api/admin/users', methods=['GET'])
@require_admin
def get_all_users() -> Tuple[Response, int]:
    """
    Get a list of all users.
    :return: Response object with user list.
    """
    return get_all_users_route()

@app.route('/api/admin/users/<user_id>/deactivate', methods=['POST'])
@require_admin
def deactivate_user(user_id: str) -> Tuple[Response, int]:
    """
    Deactivate a user by their user ID.
    :param user_id: The ID of the user to deactivate.
    :return: Response object with deactivation status.
    """
    return deactivate_user_route(user_id)

@app.route('/api/admin/users/<user_id>/activate', methods=['POST'])
@require_admin
def activate_user(user_id: str) -> Tuple[Response, int]:
    """
    Activate a user by their user ID.
    :param user_id: The ID of the user to activate.
    :return: Response object with activation status.
    """
    return activate_user_route(user_id)

@app.route('/api/admin/setup', methods=['POST'])
def setup_default_admin() -> Tuple[Response, int]:
    """
    Setup the default admin user and initial configuration.
    :return: Response object with setup status.
    """
    return setup_default_admin_route()

@app.route('/api/users/exist', methods=['GET'])
def check_users_exist() -> Tuple[Response, int]:
    """
    Check if users exist in the system.
    :return: Response object with existence check status.
    """
    return check_users_exist_route()

@app.route('/api/debug/session', methods=['GET'])
def debug_session() -> Tuple[Response, int]:
    """
    Debug endpoint to inspect the current session.
    :return: Response object with session data.
    """
    return debug_session_route()

@app.route('/api/users/search', methods=['GET'])
@require_auth
def search_users() -> Tuple[Response, int]:
    """
    Search for users in the system.
    :return: Response object with search results.
    """
    return search_users_route()

@app.route('/api/conversations', methods=['GET'])
@require_auth
def get_user_conversations() -> Tuple[Response, int]:
    """
    Get conversations for the authenticated user.
    :return: Response object with user conversations.
    """
    return get_user_conversations_route()

@app.route('/api/conversations/<conversation_id>/messages', methods=['GET'])
@require_auth
def get_conversation_messages(conversation_id: str) -> Tuple[Response, int]:
    """
    Get messages for a specific conversation.
    :param conversation_id: The ID of the conversation to retrieve messages for.
    :return: Response object with conversation messages.
    """
    return get_conversation_messages_route(conversation_id)

@app.route('/api/conversations/<conversation_id>/messages', methods=['POST'])
@require_auth
def send_message(conversation_id: str) -> Tuple[Response, int]:
    """
    Send a message to a specific conversation.
    :param conversation_id: The ID of the conversation to send a message to.
    :return: Response object with message sending status.
    """
    return send_message_route(conversation_id)

@app.route('/api/conversations', methods=['POST'])
@require_auth
def create_conversation() -> Tuple[Response, int]:
    """
    Create a new conversation for the authenticated user.
    :return: Response object with conversation creation status.
    """
    return create_conversation_route()

# TODO: Do we even use this one?
@app.route('/api/chat', methods=['GET', 'POST'])
@optional_auth
def chat_endpoint() -> Tuple[Response, int]:
    """
    Endpoint to handle chat conversations.
    :return: Response object with chat data.
    """
    if request.method == 'GET':
        return jsonify(DUMMY_CONVERSATIONS), 200
    elif request.method == 'POST':
        data = request.json
        # In a real app, you'd save this to a database
        # For now, we'll just return success
        return jsonify({"message": "Conversations saved successfully"}), 200
    else:
        return jsonify({"error": "Method not allowed"}), 405

@app.route('/api/llm_chat', methods=['GET', 'POST'])
@require_auth
def llm_agent_endpoint() -> Tuple[Response, int]:
    """
    Endpoint for LLM agent interactions.
    :return: Response object with LLM agent data.
    """
    return llm_agent_endpoint_route()

@app.route('/api/llm_chat/reset', methods=['POST'])
@optional_auth
def reset_llm_chat() -> Tuple[Response, int]:
    """
    Reset the LLM chat session
    :return: Response object indicating the reset status.
    """
    session.pop('agent_data', None)
    return jsonify({"message": "Chat session reset successfully"}), 200

@app.route('/api/time')
#@cross_origin()
def get_current_time() -> Tuple[Response, int]:
    """
    Endpoint to get the current server time.
    :return: Response object with the current time.
    """
    response = jsonify({'time': time.time()})
    return response

@app.route('/api/patients', methods=['GET', 'POST'])
def patients_endpoint() -> Tuple[Response, int]:
    """
    Endpoint to handle patient data.
    :return: Response object with patient data.
    """
    return patients_endpoint_route()

@app.route('/api/patients/<patient_id>', methods=['GET', 'PUT', 'DELETE'])
def patient_endpoint(patient_id: str) -> Tuple[Response, int]:
    """
    Endpoint to handle a specific patient by ID.
    :param patient_id: The ID of the patient to retrieve or modify.
    :return: Response object with patient data.
    """
    return patient_endpoint_route(patient_id)

@app.route('/api/patients/search', methods=['GET'])
@require_auth
def search_patients() -> Tuple[Response, int]:
    """
    Search for patients in the system.
    :return: Response object with search results.
    """
    return search_patients_route()

# Encounter endpoints
@app.route('/api/encounters', methods=['GET'])
@require_auth
def get_all_encounters() -> Tuple[Response, int]:
    """
    Get all encounters in the system.
    :return: Response object with all encounters.
    """
    return get_all_encounters_route()

@app.route('/api/encounters/search', methods=['GET'])
@require_auth
def search_encounters() -> Tuple[Response, int]:
    """
    Search for encounters in the system.
    :return: Response object with search results.
    """
    return search_encounters_route()

@app.route('/api/patients/<patient_id>/encounters', methods=['GET'])
@require_auth
def get_patient_encounters(patient_id: str) -> Tuple[Response, int]:
    """
    Get all encounters for a specific patient.
    :param patient_id: The ID of the patient to retrieve encounters for.
    :return: Response object with patient encounters.
    """
    return get_encounters_by_patient_route(patient_id)

@app.route('/api/encounters/<encounter_id>', methods=['GET'])
@require_auth
def get_encounter(encounter_id: str) -> Tuple[Response, int]:
    """
    Get a specific encounter by its ID.
    :param encounter_id: The ID of the encounter to retrieve.
    :return: Response object with encounter data.
    """
    return get_encounter_by_id_route(encounter_id)

@app.route('/api/patients/<patient_id>/encounters', methods=['POST'])
@require_auth
def create_patient_encounter(patient_id: str) -> Tuple[Response, int]:
    """
    Create a new encounter for a specific patient.
    :param patient_id: The ID of the patient to create an encounter for.
    :return: Response object with encounter creation status.
    """
    return create_encounter_route(patient_id)

@app.route('/api/encounters/<encounter_id>', methods=['PUT'])
@require_auth
def update_encounter(encounter_id: str) -> Tuple[Response, int]:
    """
    Update an existing encounter by its ID.
    :param encounter_id: The ID of the encounter to update.
    :return: Response object with encounter update status.
    """
    return update_encounter_route(encounter_id)

@app.route('/api/encounters/<encounter_id>', methods=['DELETE'])
@require_auth
def delete_encounter(encounter_id: str) -> Tuple[Response, int]:
    """
    Delete an existing encounter by its ID.
    :param encounter_id: The ID of the encounter to delete.
    :return: Response object with encounter deletion status.
    """
    return delete_encounter_route(encounter_id)

@app.route('/api/test_surrealdb', methods=['GET'])
@require_admin
def test_surrealdb() -> Tuple[Response, int]:
    """
    Test endpoint to verify SurrealDB connection
    :return: Response object with test status.
    """
    return test_surrealdb_route()

@app.route('/api/test_crud', methods=['GET'])
def test_crud() -> Tuple[Response, int]:
    """
    Test endpoint to verify CRUD operations
    :return: Response object with CRUD test status.
    """
    return test_crud_route()

@app.route('/api/intake/<patient_id>', methods=['PATCH'])
def patch_intake(patient_id: str) -> Tuple[Response, int]:
    """
    Patch the intake information for a specific patient.
    :param patient_id: The ID of the patient to patch intake information for.
    :return: Response object with intake patch status.
    """
    return patch_intake_route(patient_id)

@app.route('/api/settings', methods=['GET', 'POST'])
@require_auth
def settings() -> Tuple[Response, int]:
    """
    Endpoint to get or update user settings.
    :return: Response object with settings data or update status.
    """
    return settings_route()

@app.route('/api/usage', methods=['GET'])
@require_auth
def api_usage() -> Tuple[Response, int]:
    """
    Endpoint to get API usage statistics.
    :return: Response object with API usage data.
    """
    return get_api_usage_route()

@app.route('/api/profile', methods=['GET'])
@require_auth
def get_user_profile() -> Tuple[Response, int]:
    """
    Endpoint to get the user profile information.
    :return: Response object with user profile data.
    """
    return get_user_profile_route()

@app.route('/api/profile', methods=['POST'])
@require_auth
def update_user_profile() -> Tuple[Response, int]:
    """
    Endpoint to update the user profile information.
    :return: Response object with user profile update status.
    """
    return update_user_profile_route()

# Appointment endpoints
@app.route('/api/appointments', methods=['GET'])
@require_auth
def get_appointments() -> Tuple[Response, int]:
    """
    Get a list of appointments for the authenticated user.
    :return: Response object with appointments data.
    """
    return get_appointments_route()

@app.route('/api/appointments', methods=['POST'])
@require_auth
def create_appointment() -> Tuple[Response, int]:
    """
    Create a new appointment for the authenticated user.
    :return: Response object with appointment creation status.
    """
    return create_appointment_route()

@app.route('/api/appointments/<appointment_id>', methods=['GET'])
@require_auth
def get_appointment(appointment_id: str) -> Tuple[Response, int]:
    """
    Get details of a specific appointment by its ID.
    :param appointment_id: The ID of the appointment to retrieve.
    :return: Response object with appointment details.
    """
    return get_appointment_route(appointment_id)

@app.route('/api/appointments/<appointment_id>', methods=['PUT'])
@require_auth
def update_appointment(appointment_id: str) -> Tuple[Response, int]:
    """
    Update an existing appointment by its ID.
    :param appointment_id: The ID of the appointment to update.
    :return: Response object with appointment update status.
    """
    return update_appointment_route(appointment_id)

@app.route('/api/appointments/<appointment_id>/cancel', methods=['POST'])
@require_auth
def cancel_appointment(appointment_id: str) -> Tuple[Response, int]:
    """
    Cancel an existing appointment by its ID.
    :param appointment_id: The ID of the appointment to cancel.
    :return: Response object with appointment cancellation status.
    """
    return cancel_appointment_route(appointment_id)

@app.route('/api/appointments/<appointment_id>/confirm', methods=['POST'])
@require_auth
def confirm_appointment(appointment_id: str) -> Tuple[Response, int]:
    """
    Confirm an existing appointment by its ID.
    :param appointment_id: The ID of the appointment to confirm.
    :return: Response object with appointment confirmation status.
    """
    return confirm_appointment_route(appointment_id)

@app.route('/api/appointments/available-slots', methods=['GET'])
@require_auth
def get_available_slots() -> Tuple[Response, int]:
    """
    Get available time slots for appointments.
    :return: Response object with available slots data.
    """
    return get_available_slots_route()

@app.route('/api/appointments/types', methods=['GET'])
@require_auth
def get_appointment_types() -> Tuple[Response, int]:
    """
    Get a list of appointment types.
    :return: Response object with appointment types data.
    """
    return get_appointment_types_route()

@app.route('/api/appointments/statuses', methods=['GET'])
@require_auth
def get_appointment_statuses() -> Tuple[Response, int]:
    """
    Get a list of appointment statuses.
    :return: Response object with appointment statuses data.
    """
    return get_appointment_statuses_route()


# Webhook endpoints
@app.route('/api/webhooks', methods=['GET'])
@require_auth
def get_webhook_subscriptions() -> Tuple[Response, int]:
    """
    Get webhook subscriptions for the authenticated user.
    :return: Response object with webhook subscriptions data.
    """
    return get_webhook_subscriptions_route()


@app.route('/api/webhooks', methods=['POST'])
@require_auth
def create_webhook_subscription() -> Tuple[Response, int]:
    """
    Create a new webhook subscription.
    :return: Response object with webhook subscription creation status.
    """
    return create_webhook_subscription_route()


@app.route('/api/webhooks/<subscription_id>', methods=['GET'])
@require_auth
def get_webhook_subscription(subscription_id: str) -> Tuple[Response, int]:
    """
    Get a specific webhook subscription by its ID.
    :param subscription_id: The ID of the subscription to retrieve.
    :return: Response object with webhook subscription details.
    """
    return get_webhook_subscription_route(subscription_id)


@app.route('/api/webhooks/<subscription_id>', methods=['PUT'])
@require_auth
def update_webhook_subscription(subscription_id: str) -> Tuple[Response, int]:
    """
    Update an existing webhook subscription by its ID.
    :param subscription_id: The ID of the subscription to update.
    :return: Response object with webhook subscription update status.
    """
    return update_webhook_subscription_route(subscription_id)


@app.route('/api/webhooks/<subscription_id>', methods=['DELETE'])
@require_auth
def delete_webhook_subscription(subscription_id: str) -> Tuple[Response, int]:
    """
    Delete an existing webhook subscription by its ID.
    :param subscription_id: The ID of the subscription to delete.
    :return: Response object with webhook subscription deletion status.
    """
    return delete_webhook_subscription_route(subscription_id)


@app.route('/api/webhooks/events', methods=['GET'])
@require_auth
def get_webhook_events() -> Tuple[Response, int]:
    """
    Get available webhook events.
    :return: Response object with webhook events data.
    """
    return get_webhook_events_route()

@app.route('/api/lab_results', methods=['GET'])
@require_auth
def get_lab_results() -> Tuple[Response, int]:
    """
    Get lab results for the authenticated user.
    :return: Response object with lab results data.
    """
    lab_results_service: LabResultsService = LabResultsService(
        hematology=hematology,
        differential_hematology=differential_hematology,
        general_chemistry=general_chemistry,
        serum_proteins=serum_proteins,
    )
    return jsonify(lab_results_service.lab_results), 200


# Organizations endpoints
@app.route('/api/organizations', methods=['GET'])
def get_organizations() -> Tuple[Response, int]:
    """
    Get a list of organizations.
    :return: Response object with organizations data.
    """
    return get_organizations_route()

@app.route('/api/organizations/<org_id>', methods=['GET'])
def get_organization(org_id: str) -> Union[Tuple[Response, int], werkzeug.wrappers.response.Response]:
    """
    Get a specific organization by ID.
    :return: Response object with organization data.
    """
    print(f"get_organization: {org_id}")
    if org_id.startswith('User:'):
        print(f"redirecting to /api/organizations/user/{org_id}")
        return redirect(f'/api/organizations/user/{org_id}')
    from lib.routes.organizations import get_organization_route
    return get_organization_route(org_id)

@app.route('/api/organizations/user/<user_id>', methods=['GET'])
def get_organization_by_user_id(user_id: str) -> Tuple[Response, int]:
    """
    Get a specific organization by ID.
    :return: Response object with organization data.
    """
    from lib.routes.organizations import get_organization_by_user_id_route
    return get_organization_by_user_id_route(user_id)

@app.route('/api/organizations', methods=['POST'])
def create_organization_api() -> Tuple[Response, int]:
    """
    Create a new organization.
    :return: Response object with created organization data.
    """
    from lib.routes.organizations import create_organization_route
    return create_organization_route()

@app.route('/api/organizations/<org_id>', methods=['PUT'])
def update_organization_api(org_id: str) -> Tuple[Response, int]:
    """
    Update an organization by ID.
    :return: Response object with updated organization data.
    """
    from lib.routes.organizations import update_organization_route
    return update_organization_route(org_id)


# Register event handlers for webhook delivery
register_event_handlers()


# Register the SSE blueprint
app.register_blueprint(sse_bp)

from asgiref.wsgi import WsgiToAsgi

asgi_app = WsgiToAsgi(app)

if __name__ == '__main__': app.run(port=PORT, debug=DEBUG, host=HOST)

