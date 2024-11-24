from app.blueprints.relationships.models import Relationships
from app.app import db

class RelationshipsRepository:
    @staticmethod
    def add_friend(requester_id, receiver_id):
        new_relationship = Relationships(
            Requester_id=requester_id,
            Receiver_id=receiver_id,
            Status='pending'
        )
        db.session.add(new_relationship)
        db.session.commit()
        return new_relationship

    @staticmethod
    def update_friendship_status(requester_id, receiver_id, status):
        relationship = Relationships.query.filter_by(
            Requester_id=requester_id,
            Receiver_id=receiver_id
        ).first()
        if relationship:
            relationship.Status = status
            db.session.commit()
            return relationship
        return None

    @staticmethod
    def get_friends(user_id):
        return Relationships.query.filter(
            (Relationships.Requester_id == user_id) | (Relationships.Receiver_id == user_id),
            Relationships.status == 'accepted'
        ).all()

    @staticmethod
    def get_pending_requests(user_id):
        return Relationships.query.filter(
            Relationships.Receiver_id == user_id,
            Relationships.Status == 'pending'
        ).all()