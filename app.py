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
def chat_endpoint():
    if request.method == 'GET':
        return jsonify(DUMMY_CONVERSATIONS)
    elif request.method == 'POST':
        data = request.json
        # In a real app, you'd save this to a database
        # For now, we'll just return success
        return jsonify({"message": "Conversations saved successfully"})

@app.route('/api/llm_chat', methods=['GET', 'POST'])
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


if __name__ == '__main__':
    app.run(port=PORT, debug=DEBUG, host=HOST)

