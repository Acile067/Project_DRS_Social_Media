from app.repositories.post_repository import PostsRepository
from app.blueprints.posts.models import Post

class PostService:

    @staticmethod
    def create_post(post_id, username, txt, image_path, approved):
        if not all([post_id, username, txt, image_path, approved]):
            return {"message": "Missing data"}, 400

        existing_post = PostsRepository.get_post_by_id(post_id)
        if existing_post:
            return {"message": "Username already exists"}, 400

        post = Post(ID=post_id, Username=username, Txt=txt, ImagePath=image_path, Approved=approved)
        PostsRepository.add_post(post)
        return {"message": "Created"}, 201

    @staticmethod
    def edit_post(post_id, username, txt, image_path, approved):
        post = PostsRepository.get_post_by_id(post_id)
        if not post:
            return {"message": "Post not found"}, 404

        post.ID = id
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
