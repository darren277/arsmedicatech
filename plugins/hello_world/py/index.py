""""""
from flask import Blueprint, jsonify

plugin_bp = Blueprint('hello_world', __name__)

@plugin_bp.route('/hello_world/foo')
def foo():
    return jsonify(message='Foo plugin active!')
