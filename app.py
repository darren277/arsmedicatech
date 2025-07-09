""""""
import time
from flask import Flask, jsonify, request, session
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics

from lib.dummy_data import DUMMY_CONVERSATIONS
from lib.routes.chat import create_conversation_route, send_message_route, get_conversation_messages_route, \
    get_user_conversations_route
from lib.routes.llm_agent import llm_agent_endpoint_route
from lib.routes.patients import patch_intake_route, search_patients_route, patient_endpoint_route, \
    patients_endpoint_route
from lib.routes.testing import test_surrealdb_route, test_crud_route, debug_session_route
from lib.routes.users import search_users_route, check_users_exist_route, setup_default_admin_route, \
    activate_user_route, deactivate_user_route, get_all_users_route, change_password_route, get_current_user_info_route, \
    logout_route, register_route, login_route, settings_route, get_api_usage_route
from lib.services.auth_decorators import require_auth, require_admin, optional_auth
from settings import PORT, DEBUG, HOST, FLASK_SECRET_KEY

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:3012", "http://127.0.0.1:3012", "https://demo.arsmedicatech.com"], "supports_credentials": True}})

app.secret_key = FLASK_SECRET_KEY

metrics = PrometheusMetrics(app)

app.config['CORS_HEADERS'] = 'Content-Type'

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


from asgiref.wsgi import WsgiToAsgi

asgi_app = WsgiToAsgi(app)

#if __name__ == '__main__': app.run(port=PORT, debug=DEBUG, host=HOST)

