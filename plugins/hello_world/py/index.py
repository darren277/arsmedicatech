
""""""
from flask import Blueprint, jsonify

hello_world_bp = Blueprint('hello_world', __name__)

@hello_world_bp.route('/hello_world/foo')
def foo():
    return jsonify(message='Foo plugin active!')
