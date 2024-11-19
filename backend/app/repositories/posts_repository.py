from app.blueprints.posts.models import Post
from app.app import db


class PostsRepository:
    @staticmethod
    def get_all_posts_for_user(username):
        return Post.query.filter_by(Username=username).all()

    #@staticmethod
    #def get_user_by_username(username):
        #return User.query.filter_by(Username=username).first()

    @staticmethod
    def add_post(post):
        db.session.add(post)
        db.session.commit()

    @staticmethod
    def update_post(post):
        db.session.commit()