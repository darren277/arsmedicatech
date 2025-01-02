""""""
import os
import time
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"data": "Hello World"})


@app.route('/time')
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

@app.route('/patients', methods=['GET'])
def get_patients():
    # fetch from db...
    patients = [{"id": 1, "first_name": "John", "last_name": "Doe", "age": 45}, {"id": 2, "first_name": "Jane", "last_name": "Doe", "age": 35}]
    return jsonify(patients)

@app.route('/patients/<patient_id>', methods=['GET'])
def get_patient(patient_id):
    print("Patient ID:", patient_id)
    if patient_id == '1':
        return jsonify({"id": 1, "first_name": "John", "last_name": "Doe", "age": 45, "history": john_doe_history})
    elif patient_id == '2':
        return jsonify({"id": 2, "first_name": "Jane", "last_name": "Doe", "age": 35, "history": jane_doe_history})
    else:
        return jsonify({"result": "Patient not found."})


if __name__ == '__main__':
    app.run(port=os.environ.get('PORT', 5000), debug=os.environ.get('DEBUG', True), host=os.environ.get('HOST', '0.0.0.0'))
