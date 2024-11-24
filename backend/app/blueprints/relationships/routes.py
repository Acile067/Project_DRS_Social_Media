from flask import Blueprint, request, jsonify
from app.blueprints.auth.auth import token_required
from app.services.relationships_service import RelationshipsService

relationships_bp = Blueprint('relationships_bp', __name__)

@relationships_bp.route('/addfriend', methods=["POST"])
@token_required
def add_friend_users(user_data):
    data = request.get_json()
    username_id = user_data.get('user_id')
    receiver_id = data.get('receiver_id')

    if not receiver_id:
        return jsonify({'message': 'Receiver ID is required'}), 400

    try:
        new_request = RelationshipsService.send_friend_request(username_id, receiver_id)
        return jsonify({'message': 'Friend request sent', 'request': str(new_request)}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@relationships_bp.route('/respondfriend', methods=["POST"])
@token_required
def respond_friend_request(user_data):
    data = request.get_json()
    requester_id = data.get('requester_id')
    status = data.get('status')
    username_id = user_data.get('user_id')

    if not requester_id or not status:
        return jsonify({'message': 'Requester ID and status are required'}), 400

    try:
        updated_relationship = RelationshipsService.respond_to_friend_request(requester_id, username_id, status)
        if updated_relationship:
            return jsonify({'message': f'Friend request {status}'}), 200
        return jsonify({'message': 'No such friend request found'}), 404
    except ValueError as e:
        return jsonify({'message': str(e)}), 400
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@relationships_bp.route('/friends', methods=["GET"])
@token_required
def list_friends(user_data):
    try:
        friends = RelationshipsService.get_user_friends(user_data['user_id'])
        return jsonify({'friends': friends}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@relationships_bp.route('/friendrequests', methods=["GET"])
@token_required
def list_friend_requests(user_data):
    try:
        pending_requests = RelationshipsService.get_user_pending_requests(user_data['user_id'])
        return jsonify({'pending_requests': pending_requests}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500