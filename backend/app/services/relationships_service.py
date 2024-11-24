import jwt
import datetime
from app.repositories.relationships_repository import RelationshipsRepository
from app.blueprints.relationships.models import Relationships

SECRET_KEY = 'your_secret_key_here'

class RelationshipsService:
    @staticmethod
    def send_friend_request(requester_id, receiver_id):
        return RelationshipsRepository.add_friend(requester_id, receiver_id)

    @staticmethod
    def respond_to_friend_request(requester_id, receiver_id, status):
        if status not in ['accepted', 'rejected']:
            raise ValueError("Invalid status")
        return RelationshipsRepository.update_friendship_status(requester_id, receiver_id, status)

    @staticmethod
    def get_user_friends(user_id):
        friends = RelationshipsRepository.get_friends(user_id)
        return [{'requester_id': r.Requester_id, 'receiver_id': r.Receiver_id} for r in friends]

    @staticmethod
    def get_user_pending_requests(user_id):
        pending_requests = RelationshipsRepository.get_pending_requests(user_id)
        return [{'requester_id': r.Requester_id, 'receiver_id': r.Receiver_id} for r in pending_requests]