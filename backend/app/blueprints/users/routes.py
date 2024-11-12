from flask import Blueprint, request, jsonify
from app.blueprints.auth.auth import token_required
from app.services.user_service import UserService

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/users', methods=["GET"])
def get_all_users():
    response, status = UserService.get_all_users()
    return jsonify(response), status

@users_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    response, status = UserService.login_user(data.get('username'), data.get('password'))
    return jsonify(response), status

@users_bp.route('/register', methods=['POST'])
@token_required
def register(user_data):
    is_admin = user_data.get('isAdmin')
    if not(is_admin == 'yes'):
        return jsonify({"message": "Unauthorized"}),401

    data = request.json
    response, status = UserService.register_user(data.get('username'), data.get('name'), data.get('lastname'), data.get('password'), data.get('email'),data.get('address'),data.get('city'),data.get('state'),data.get('phonenumber'))
    return jsonify(response), status

@users_bp.route('/edituserprofile', methods=['GET', 'POST'])
@token_required
def edit_user_profile(user_data):
    username_id = user_data.get('user_id')
    if request.method == 'GET':
        # Prikaz podataka o korisniku
        response, status = UserService.get_user_by_username(username_id)
        return {"data": response}, status

    elif request.method == 'POST':
        data = request.json
        response, status = UserService.edit_user_profile(username_id, data.get('username'), data.get('name'), data.get('lastname'), data.get('password'), data.get('email'),data.get('address'),data.get('city'),data.get('state'),data.get('phonenumber'))
        return jsonify(response), status