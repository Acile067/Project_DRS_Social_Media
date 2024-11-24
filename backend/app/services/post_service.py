from app.repositories.posts_repository import PostsRepository
from app.blueprints.posts.models import Post

from app.repositories.user_repository import UserRepository


class PostService:

    @staticmethod
    def get_all_posts():
        posts = PostsRepository.get_all_posts()
        posts_list = [{"post_id": post.ID, "username": post.Username, "txt": post.Txt, "image_path": post.ImagePath, "approved": post.Approved} for post in posts]

        return {"data": posts_list}, 200

    @staticmethod
    def get_all_posts_for_user(username):
        posts = PostsRepository.get_all_posts_for_user(username)
        posts_list = [{"post_id": post.ID, "username": post.Username, "txt": post.Txt, "image_path": post.ImagePath, "approved": post.Approved} for post in posts]
        return {"data": posts_list}, 200

    @staticmethod
    def create_post(username, txt, image_path):
        if not (txt or image_path):
            return {"message": "Missing data"}, 400

        post = Post(Username=username, Txt=txt, ImagePath=image_path)
        PostsRepository.add_post(post)
        return {"message": "Created"}, 201

    @staticmethod
    def edit_post(post_id, username, txt, image_path, approved):
        post = PostsRepository.get_post_by_id(post_id)
        if not post:
            return {"message": "Post not found"}, 404

        post.ID = post_id
        post.Username = username
        post.Txt = txt
        post.ImagePath = image_path
        post.Approved = approved

        PostsRepository.update_post(post)

        return {"message": "Ok"}, 200

    @staticmethod
    def delete_post(post_id):
        post = PostsRepository.get_post_by_id(post_id)

        PostsRepository.delete_post(post)

        return {"message": "Ok"}, 200

    @staticmethod
    def get_post_by_id(post_id):
        post = PostsRepository.get_post_by_id(post_id)

        if post:
            return {
                "post_id": post.ID,
                "username": post.Username,
                "txt": post.Txt,
                "image_path": post.ImagePath,
                "approved" : post.Approved
            }, 200

        return {"message": "Post not found"}, 404

    @staticmethod
    def get_username(user_id):
        user = UserRepository.get_user_by_username(user_id)
        username = user.Username
        return username
