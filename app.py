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


if __name__ == '__main__':
    app.run(port=os.environ.get('PORT', 5000), debug=os.environ.get('DEBUG', True), host=os.environ.get('HOST', '0.0.0.0'))
