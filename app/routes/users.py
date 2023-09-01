from flask import Blueprint, jsonify
from . import routes  # Importe o Blueprint 'routes' que criamos anteriormente

@routes.route('/users', methods=['GET'])
def get_users():
    # Por enquanto, apenas retornando uma mensagem
    return jsonify({"message": "List of users"})
