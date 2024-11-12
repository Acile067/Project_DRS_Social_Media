from app.blueprints.users.models import User
from app.app import db


class UserRepository:
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(Username=username).first()

    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def update_user(user):
        db.session.commit()