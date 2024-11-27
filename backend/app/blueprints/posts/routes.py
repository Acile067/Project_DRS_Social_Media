import uuid

from flask import Blueprint, request, jsonify, current_app
from app.blueprints.auth.auth import token_required
from app.services.post_service import PostService
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
import os
from app.app import db, socketio  # Import socketio
from flask_socketio import emit  # Import emit



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
@cross_origin()
@token_required
def create(user_data):
    current_user_id = user_data.get('user_id')
    current_user_username = PostService.get_username(current_user_id)

    print("Received username:", current_user_username)
    txt = request.form.get('txt')  # Get the text from the form data
    image = request.files.get('image')  # Get the uploaded image
    image_uuid = None

    if image and allowed_file(image.filename):
        # Generate a unique filename using UUID
        extension = secure_filename(image.filename).rsplit('.', 1)[1].lower()
        image_uuid = str(uuid.uuid4())
        unique_filename = f"{image_uuid}.{extension}"
        upload_folder = current_app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        image_path = os.path.join(upload_folder, unique_filename)

        # Save the image to the server
        image.save(image_path)
    print("Generated UUID for image:", image_uuid)
    print("Received text:", txt)

    response, status = PostService.create_post(current_user_username, txt, image_uuid)

    socketio.emit('new_post', {
        'username': current_user_username,
        'txt': txt,
        'image_path': image_uuid
    })

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




