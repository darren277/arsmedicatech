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
from settings import PORT, DEBUG, HOST, logger, OPENAI_API_KEY

app = Flask(__name__)
CORS(app)

metrics = PrometheusMetrics(app)

app.config['CORS_HEADERS'] = 'Content-Type'

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
    agent = session.get('agent')

    if not agent:
        agent = LLMAgent(api_key=OPENAI_API_KEY)
        agent.add_tool(blood_pressure_decision_tree_lookup, tool_definition_bp)
        session['agent'] = agent

    response = agent.complete(prompt)

    return jsonify(response)


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
def get_patient(patient_id):
    print("Patient ID:", patient_id)
    if patient_id == '1':
        return jsonify({"id": 1, "first_name": "John", "last_name": "Doe", "age": 45, "history": john_doe_history})
    elif patient_id == '2':
        return jsonify({"id": 2, "first_name": "Jane", "last_name": "Doe", "age": 35, "history": jane_doe_history})
    else:
        return jsonify({"result": "Patient not found."})


@app.route('/api/test_surrealdb', methods=['GET'])
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

