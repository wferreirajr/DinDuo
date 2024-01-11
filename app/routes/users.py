from flask import Blueprint, jsonify, request
from . import routes  # Importe o Blueprint 'routes' que criamos anteriormente

@routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    from app.models.user import User
    
    new_user = User(
        email=data['email'],
        password=data['password'],  # Em um ambiente real, você deve HASH a senha antes de armazená-la
        full_name=data['full_name'],
        family_id=data.get('family_id'),
        role=data.get('role'),
        tenant_id=data.get('tenant_id')
    )

    from app import db
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created!"}), 201


