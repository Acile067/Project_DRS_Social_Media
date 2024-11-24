from flask import Blueprint, request, jsonify, current_app
from app.blueprints.auth.auth import token_required
from app.services.post_service import PostService
from app.repositories.user_repository import UserRepository
from werkzeug.utils import secure_filename
import os


from app.repositories.posts_repository import PostsRepository

posts_bp = Blueprint('posts_bp', __name__)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

@posts_bp.route('/getallposts', methods=["GET"])
@token_required
def get_all_posts():
    response, status = PostService.get_all_posts()
    return jsonify(response), status

@posts_bp.route('/getalluserposts', methods=['GET'])
@token_required
def get_all_posts_for_user():
    username = request.args.get('username')
    response, status = PostService.get_all_posts_for_user(username)
    return jsonify(response), status

@posts_bp.route('/createpost', methods=['POST'])
@token_required
def create(user_data):
    current_user_id = user_data.get('user_id')
    current_user = UserRepository.get_user_by_username(current_user_id)
    print("dsg:", current_user)
    print("Received username:", current_user.Username)
    #data = request.get_json()
    txt = request.form.get('txt')  # Get the text from the form data
    image = request.files.get('image')  # Get the uploaded image
    print("Received txt:", txt)
    print("Received img:", image)
    #print("Received data:", data)
    relative_image_path = None
    # Check if the file is allowed
    if image and allowed_file(image.filename):
        # Secure the filename to avoid directory traversal attacks
        filename = secure_filename(image.filename)
        upload_folder = current_app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)

        # Save the image to the server
        image.save(image_path)

        # Save the relative path to the database (you can store just the filename or relative path)
        relative_image_path = os.path.join('images', filename)

    print("Received img path:", relative_image_path)
    print("Received text:", txt)


    response, status = PostService.create_post(current_user.Username,txt,
                                               relative_image_path)
    return jsonify(response), status

@posts_bp.route('/editpost', methods=['GET, POST'])
@token_required
def edit():
    post_id = request.args.get('post_id')
    if request.method == 'GET':
        response, status = PostService.get_post_by_id(post_id)
        return {"data": response}, status

    elif request.method == 'POST':
        data = request.json
        response, status = PostService.edit_post(data.get('post_id'),data.get('username'),data.get('txt'),
                                               data.get('image_path'),data.get('approved'))
        return jsonify(response), status




