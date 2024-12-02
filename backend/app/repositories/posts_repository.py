from app.blueprints.posts.models import Post
from app.app import db


class PostsRepository:

    @staticmethod
    def get_all_posts():
        return Post.query.all()

    @staticmethod
    def get_all_approved_posts_for_user(username):
        return Post.query.filter_by(Username=username, Approved="yes").order_by(Post.CreatedAt.desc()).all()

    @staticmethod
    def get_post_by_id(post_id):
        return Post.query.filter_by(ID=post_id).first()

    @staticmethod
    def get_unapproved_posts():
        return Post.query.filter_by(Approved='no').all()

    @staticmethod
    def add_post(post):
        db.session.add(post)
        db.session.commit()

    @staticmethod
    def update_post():
        db.session.commit()

    @staticmethod
    def delete_post(post):

        db.session.delete(post)
        db.session.commit()
