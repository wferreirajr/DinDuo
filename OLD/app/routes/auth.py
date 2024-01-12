from flask import Blueprint, jsonify
from . import routes  # Importe o Blueprint 'routes' que criamos anteriormente

@routes.route('/login', methods=['GET'])
def login():
    return jsonify({"message": "Login"})
