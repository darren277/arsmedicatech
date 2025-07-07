""""""
import time
from flask import Flask, jsonify, request, session
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics

from lib.db.surreal import DbController
from lib.llm.agent import LLMAgent
from lib.llm.trees import blood_pressure_decision_tree_lookup, tool_definition_bp
from lib.models.patient import search_patient_history, create_schema, add_some_placeholder_encounters, \
    add_some_placeholder_patients
from lib.services.user_service import UserService
from lib.services.auth_decorators import require_auth, require_admin, require_doctor, require_nurse, optional_auth, get_current_user
from settings import PORT, DEBUG, HOST, logger, OPENAI_API_KEY, FLASK_SECRET_KEY

app = Flask(__name__)
CORS(app)

app.secret_key = FLASK_SECRET_KEY

metrics = PrometheusMetrics(app)

app.config['CORS_HEADERS'] = 'Content-Type'

# Global tool registry - these don't need to be in session
GLOBAL_TOOL_DEFINITIONS = []
GLOBAL_TOOL_FUNC_DICT = {}

def register_tools():
    """Register tools globally - only needs to be done once"""
    global GLOBAL_TOOL_DEFINITIONS, GLOBAL_TOOL_FUNC_DICT
    
    # Create a temporary agent to get the tool definitions
    temp_agent = LLMAgent(api_key=OPENAI_API_KEY)
    temp_agent.add_tool(blood_pressure_decision_tree_lookup, tool_definition_bp)
    
    GLOBAL_TOOL_DEFINITIONS = temp_agent.tool_definitions
    GLOBAL_TOOL_FUNC_DICT = temp_agent.tool_func_dict

# Register tools on startup
register_tools()

@app.route('/api/', methods=['GET'])
def hello_world():
    return jsonify({"data": "Hello World"})

# Authentication endpoints
@app.route('/api/auth/register', methods=['POST'])
def register():
    """Register a new user account"""
    print("[DEBUG] Registration request received")
    data = request.json
    print(f"[DEBUG] Registration data: {data}")
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    
    print(f"[DEBUG] Registration fields - username: {username}, email: {email}, first_name: {first_name}, last_name: {last_name}")
    
    if not all([username, email, password]):
        return jsonify({"error": "Username, email, and password are required"}), 400
    
    user_service = UserService()
    user_service.connect()
    try:
        print("[DEBUG] Calling user_service.create_user")
        success, message, user = user_service.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        
        print(f"[DEBUG] User creation result - success: {success}, message: {message}")
        if success:
            print(f"[DEBUG] User created successfully: {user.id}")
            return jsonify({
                "message": message,
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role": user.role
                }
            }), 201
        else:
            print(f"[DEBUG] User creation failed: {message}")
            return jsonify({"error": message}), 400
    finally:
        user_service.close()

@app.route('/api/auth/login', methods=['POST'])
def login():
    """Authenticate user and create session"""
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    username = data.get('username')
    password = data.get('password')
    
    if not all([username, password]):
        return jsonify({"error": "Username and password are required"}), 400
    
    user_service = UserService()
    user_service.connect()
    try:
        success, message, user_session = user_service.authenticate_user(username, password)
        
        if success:
            # Store token in session
            session['auth_token'] = user_session.token
            
            return jsonify({
                "message": message,
                "token": user_session.token,
                "user": {
                    "id": user_session.user_id,
                    "username": user_session.username,
                    "role": user_session.role
                }
            }), 200
        else:
            return jsonify({"error": message}), 401
    finally:
        user_service.close()

@app.route('/api/auth/logout', methods=['POST'])
@require_auth
def logout():
    """Logout user and invalidate session"""
    token = session.get('auth_token')
    if token:
        user_service = UserService()
        user_service.connect()
        try:
            user_service.logout(token)
        finally:
            user_service.close()
    
    session.pop('auth_token', None)
    return jsonify({"message": "Logged out successfully"}), 200

@app.route('/api/auth/me', methods=['GET'])
@require_auth
def get_current_user_info():
    """Get current authenticated user information"""
    user_service = UserService()
    user_service.connect()
    try:
        user = user_service.get_user_by_id(get_current_user().user_id)
        if user:
            return jsonify({
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role": user.role,
                    "is_active": user.is_active,
                    "created_at": user.created_at
                }
            }), 200
        else:
            return jsonify({"error": "User not found"}), 404
    finally:
        user_service.close()

@app.route('/api/auth/change-password', methods=['POST'])
@require_auth
def change_password():
    """Change user password"""
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    current_password = data.get('current_password')
    new_password = data.get('new_password')
    
    if not all([current_password, new_password]):
        return jsonify({"error": "Current password and new password are required"}), 400
    
    user_service = UserService()
    user_service.connect()
    try:
        success, message = user_service.change_password(
            get_current_user().user_id,
            current_password,
            new_password
        )
        
        if success:
            return jsonify({"message": message}), 200
        else:
            return jsonify({"error": message}), 400
    finally:
        user_service.close()

# Admin endpoints
@app.route('/api/admin/users', methods=['GET'])
@require_admin
def get_all_users():
    """Get all users (admin only)"""
    user_service = UserService()
    user_service.connect()
    try:
        users = user_service.get_all_users()
        return jsonify({
            "users": [
                {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role": user.role,
                    "is_active": user.is_active,
                    "created_at": user.created_at
                }
                for user in users
            ]
        }), 200
    finally:
        user_service.close()

@app.route('/api/admin/users/<user_id>/deactivate', methods=['POST'])
@require_admin
def deactivate_user(user_id):
    """Deactivate a user account (admin only)"""
    user_service = UserService()
    user_service.connect()
    try:
        success, message = user_service.deactivate_user(user_id)
        if success:
            return jsonify({"message": message}), 200
        else:
            return jsonify({"error": message}), 400
    finally:
        user_service.close()

@app.route('/api/admin/users/<user_id>/activate', methods=['POST'])
@require_admin
def activate_user(user_id):
    """Activate a user account (admin only)"""
    user_service = UserService()
    user_service.connect()
    try:
        success, message = user_service.activate_user(user_id)
        if success:
            return jsonify({"message": message}), 200
        else:
            return jsonify({"error": message}), 400
    finally:
        user_service.close()

@app.route('/api/admin/setup', methods=['POST'])
def setup_default_admin():
    """Setup default admin user (only works if no users exist)"""
    user_service = UserService()
    user_service.connect()
    try:
        success, message = user_service.create_default_admin()
        if success:
            return jsonify({"message": message}), 200
        else:
            return jsonify({"error": message}), 400
    finally:
        user_service.close()

id, name, lastMessage, avatar, messages, sender, text = 'id', 'name', 'lastMessage', 'avatar', 'messages', 'sender', 'text'

DUMMY_CONVERSATIONS = [
  {
    "id": 1,
    "name": "Jane Smith",
    "lastMessage": "Sounds good!",
    "avatar": "https://via.placeholder.com/40",
    "messages": [
      { "sender": "Jane Smith", "text": "Hi Dr. Carvolth, can we schedule an appointment?" },
      { "sender": "Me", "text": "Sure, does tomorrow at 3pm work?" },
      { "sender": "Jane Smith", "text": "Sounds good!" },
    ],
  },
  {
    "id": 2,
    "name": "John Doe",
    "lastMessage": "Alright, thank you so much!",
    "avatar": "https://via.placeholder.com/40",
    "messages": [
      { "sender": "John Doe", "text": "Hello Dr. Carvolth, I have a question about my medication." },
      { "sender": "Me", "text": "Sure, what's on your mind?" },
      { "sender": "John Doe", "text": "Should I continue at the same dose?" },
      { "sender": "Me", "text": "Yes, please stay on the same dose until our next check-up." },
      { "sender": "John Doe", "text": "Alright, thank you so much!" },
    ],
  },
  {
    "id": 3,
    "name": "Emily Johnson",
    "lastMessage": "Will do, thanks!",
    "avatar": "https://via.placeholder.com/40",
    "messages": [
      { "sender": "Emily Johnson", "text": "Dr. Carvolth, when is my next appointment?" },
      { "sender": "Me", "text": "Next Tuesday at 2 PM, does that still work?" },
      { "sender": "Emily Johnson", "text": "Yes, that's perfect! Thank you!" },
      { "sender": "Me", "text": "Great, see you then." },
      { "sender": "Emily Johnson", "text": "Will do, thanks!" },
    ],
  }
]

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
    if request.method == 'GET':
        #conversation_history = session.get('conversation_history', [])
        conversation_history = DUMMY_CONVERSATIONS
        return jsonify(conversation_history)
    data = request.json

    print("Received data:", data)

    prompt = data.get('prompt')
    
    # Get or create agent from session
    agent_data = session.get('agent_data')
    
    if agent_data:
        # Recreate agent from session data
        agent = LLMAgent.from_dict(
            agent_data, 
            api_key=OPENAI_API_KEY,
            tool_definitions=GLOBAL_TOOL_DEFINITIONS,
            tool_func_dict=GLOBAL_TOOL_FUNC_DICT
        )
    else:
        # Create new agent
        agent = LLMAgent(api_key=OPENAI_API_KEY)
        agent.tool_definitions = GLOBAL_TOOL_DEFINITIONS
        agent.tool_func_dict = GLOBAL_TOOL_FUNC_DICT

    # Process the prompt
    response = agent.complete(prompt)
    
    # Save updated agent state to session
    session['agent_data'] = agent.to_dict()

    return jsonify(response)

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

john_doe_history = [
    {"date": "2021-01-01", "note": "Patient has a fever."},
    {"date": "2021-01-02", "note": "Patient has a cough."},
    {"date": "2021-01-03", "note": "Patient has a headache."}
]

jane_doe_history = [
    {"date": "2021-01-01", "note": "Patient has a fever."},
    {"date": "2021-01-02", "note": "Patient has a cough."},
    {"date": "2021-01-03", "note": "Patient has a headache."}
]

@app.route('/api/patients', methods=['GET'])
@require_auth
def get_patients():
    # This is your existing endpoint, using the mock DB controller.
    db = DbController()
    db.connect()
    results = db.select_many('Patient')
    db.close()
    if results and isinstance(results, list) and len(results) > 0:
        return jsonify(results[0].get('result', []))
    return jsonify([])


@app.route('/api/patients/search', methods=['GET'])
@require_auth
def search_patients():
    """
    API endpoint to search patient histories via FTS.
    Accepts a 'q' query parameter.
    e.g., /api/patients/search?q=headache
    """
    search_term = request.args.get('q', '')
    if not search_term or len(search_term) < 2:
        return jsonify({"message": "Please provide a search term with at least 2 characters."}), 400

    results = search_patient_history(search_term)
    return jsonify(results)



@app.route('/api/patients/<patient_id>', methods=['GET'])
@require_auth
def get_patient(patient_id):
    print("Patient ID:", patient_id)
    if patient_id == '1':
        return jsonify({"id": 1, "first_name": "John", "last_name": "Doe", "age": 45, "history": john_doe_history})
    elif patient_id == '2':
        return jsonify({"id": 2, "first_name": "Jane", "last_name": "Doe", "age": 35, "history": jane_doe_history})
    else:
        return jsonify({"result": "Patient not found."})


@app.route('/api/test_surrealdb', methods=['GET'])
@require_admin
def test_surrealdb():
    db = DbController()
    db.connect()

    #create_schema()

    add_some_placeholder_patients(db)

    results = db.select_many('Patient')
    logger.info("RESULTS: " + str(results))
    return jsonify({"message": "Test completed."})


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG, host=HOST)

