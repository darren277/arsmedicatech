""""""
import time
from flask import Flask, jsonify, request, session
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics

from lib.db.surreal import DbController
from lib.llm.agent import LLMAgent
from lib.llm.trees import blood_pressure_decision_tree_lookup, tool_definition_bp
from lib.models.patient import search_patient_history, create_schema, add_some_placeholder_encounters, \
    add_some_placeholder_patients, get_patient_by_id, update_patient, delete_patient, create_patient, get_all_patients
from lib.services.user_service import UserService
from lib.services.auth_decorators import require_auth, require_admin, require_doctor, require_nurse, optional_auth, get_current_user
from settings import PORT, DEBUG, HOST, logger, OPENAI_API_KEY, FLASK_SECRET_KEY

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000", "http://localhost:3012", "http://127.0.0.1:3012", "https://demo.arsmedicatech.com"], "supports_credentials": True}})

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
    role = data.get('role', 'patient')
    print(f"[DEBUG] Registration fields - username: {username}, email: {email}, first_name: {first_name}, last_name: {last_name}, role: {role}")
    
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
            last_name=last_name,
            role=role
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
    print("[DEBUG] Login request received")
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    username = data.get('username')
    password = data.get('password')
    
    print(f"[DEBUG] Login attempt for username: {username}")
    
    if not all([username, password]):
        return jsonify({"error": "Username and password are required"}), 400
    
    user_service = UserService()
    user_service.connect()
    try:
        success, message, user_session = user_service.authenticate_user(username, password)
        
        print(f"[DEBUG] Authentication result - success: {success}, message: {message}")
        
        if success:
            # Store token in session
            session['auth_token'] = user_session.token
            print(f"[DEBUG] Stored session token: {user_session.token[:10]}...")
            
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

@app.route('/api/users/exist', methods=['GET'])
def check_users_exist():
    """Check if any users exist (public endpoint)"""
    user_service = UserService()
    user_service.connect()
    try:
        users = user_service.get_all_users()
        print(f"[DEBUG] Found {len(users)} users in database")
        for user in users:
            print(f"[DEBUG] User: {user.username} (ID: {user.id}, Role: {user.role}, Active: {user.is_active})")
        return jsonify({"users_exist": len(users) > 0, "user_count": len(users)})
    finally:
        user_service.close()

@app.route('/api/debug/session', methods=['GET'])
def debug_session():
    """Debug endpoint to check session state"""
    print(f"[DEBUG] Session data: {dict(session)}")
    print(f"[DEBUG] Request headers: {dict(request.headers)}")
    return jsonify({
        "session": dict(session),
        "headers": dict(request.headers)
    })

@app.route('/api/users/search', methods=['GET'])
@require_auth
def search_users():
    """Search for users (authenticated users only)"""
    print("[DEBUG] User search request received")
    query = request.args.get('q', '').strip()
    print(f"[DEBUG] Search query: '{query}'")
    
    user_service = UserService()
    user_service.connect()
    try:
        # Get all users and filter by search query
        all_users = user_service.get_all_users()
        
        # Filter users based on search query
        filtered_users = []
        for user in all_users:
            # Skip inactive users
            if not user.is_active:
                continue
                
            # Skip the current user
            if user.id == get_current_user().user_id:
                continue
                
            # Search in username, first_name, last_name, and email
            searchable_text = f"{user.username} {user.first_name or ''} {user.last_name or ''} {user.email or ''}".lower()
            
            if not query or query.lower() in searchable_text:
                filtered_users.append({
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role": user.role,
                    "display_name": f"{user.first_name or ''} {user.last_name or ''}".strip() or user.username,
                    "avatar": f"https://ui-avatars.com/api/?name={user.first_name or user.username}&background=random"
                })
        
        # Limit results to 20 users
        filtered_users = filtered_users[:20]
        
        return jsonify({
            "users": filtered_users,
            "total": len(filtered_users)
        }), 200
        
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

@app.route('/api/patients', methods=['GET', 'POST'])
def patients_endpoint():
    if request.method == 'GET':
        # Get all patients
        patients = get_all_patients()
        return jsonify(patients)
    elif request.method == 'POST':
        # Create a new patient
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        # Validate required fields
        required_fields = ['first_name', 'last_name']
        for field in required_fields:
            if not data.get(field):
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        patient = create_patient(data)
        if patient:
            return jsonify(patient), 201
        else:
            return jsonify({"error": "Failed to create patient"}), 500


@app.route('/api/patients/<patient_id>', methods=['GET', 'PUT', 'DELETE'])
def patient_endpoint(patient_id):
    print(f"[DEBUG] Patient endpoint called with patient_id: {patient_id}")
    print(f"[DEBUG] Request method: {request.method}")
    
    if request.method == 'GET':
        # Get a specific patient
        print(f"[DEBUG] Getting patient with ID: {patient_id}")
        patient = get_patient_by_id(patient_id)
        print(f"[DEBUG] Patient result: {patient}")
        if patient:
            return jsonify(patient)
        else:
            return jsonify({"error": "Patient not found"}), 404
    
    elif request.method == 'PUT':
        # Update a patient
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        patient = update_patient(patient_id, data)
        if patient:
            return jsonify(patient)
        else:
            return jsonify({"error": "Patient not found or update failed"}), 404
    
    elif request.method == 'DELETE':
        # Delete a patient
        result = delete_patient(patient_id)
        if result:
            return jsonify({"message": "Patient deleted successfully"})
        else:
            return jsonify({"error": "Patient not found or delete failed"}), 404


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


@app.route('/api/test_surrealdb', methods=['GET'])
@require_admin
def test_surrealdb():
    db = DbController()
    db.connect()

    #create_schema()

    add_some_placeholder_patients(db)

    results = db.select_many('patient')
    logger.info("RESULTS: " + str(results))
    return jsonify({"message": "Test completed."})


@app.route('/api/test_crud', methods=['GET'])
def test_crud():
    """Test endpoint to verify CRUD operations"""
    try:
        # Test creating a patient
        test_patient_data = {
            "first_name": "Test",
            "last_name": "Patient",
            "date_of_birth": "1990-01-01",
            "sex": "M",
            "phone": "555-1234",
            "email": "test@example.com",
            "location": ["Test City", "Test State", "Test Country", "12345"]
        }
        
        created_patient = create_patient(test_patient_data)
        if not created_patient:
            return jsonify({"error": "Failed to create patient"}), 500
        
        patient_id = created_patient.get('demographic_no')
        
        # Test reading the patient
        read_patient = get_patient_by_id(patient_id)
        if not read_patient:
            return jsonify({"error": "Failed to read patient"}), 500
        
        # Test updating the patient
        update_data = {"phone": "555-5678"}
        updated_patient = update_patient(patient_id, update_data)
        if not updated_patient:
            return jsonify({"error": "Failed to update patient"}), 500
        
        # Test deleting the patient
        delete_result = delete_patient(patient_id)
        if not delete_result:
            return jsonify({"error": "Failed to delete patient"}), 500
        
        return jsonify({
            "message": "CRUD operations test completed successfully",
            "created": created_patient,
            "read": read_patient,
            "updated": updated_patient,
            "deleted": delete_result
        })
        
    except Exception as e:
        logger.error(f"CRUD test failed: {e}")
        return jsonify({"error": f"CRUD test failed: {str(e)}"}), 500


@app.route('/api/intake/<patient_id>', methods=['PATCH'])
def patch_intake(patient_id):
    payload = request.get_json()
    print(f"[DEBUG] Patching patient {patient_id} with payload: {payload}")

    # Map 'User:' to patient ID if needed
    patient_id = patient_id.replace('User:', '')

    result = update_patient(patient_id, payload)
    print(f"[DEBUG] Update result: {result}")
    if not result:
        logger.error(f"Failed to update patient {patient_id}: {result}")
        return jsonify({"error": "Failed to update patient"}), 400
    return jsonify({'ok': True}), 200


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG, host=HOST)

