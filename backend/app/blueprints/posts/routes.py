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

@posts_bp.route('/approvedpostsforuser', methods=['GET'])
@token_required
def get_all_approved_posts_for_user(user_data):
    current_user_id = user_data.get('user_id')
    current_user_username = PostService.get_username(current_user_id)
    response, status = PostService.get_all_approved_posts_for_user(current_user_username)
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
    post_id = str(uuid.uuid4())
    response, status = PostService.create_post(post_id ,current_user_username, txt, image_uuid)

    print(post_id)
    socketio.emit('new_post', {
        'post_id': post_id,  # Include post_id
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

@posts_bp.route('/unapproved', methods=['GET'])
@cross_origin()
def get_unapproved_posts():
    unapproved_posts = PostService.get_unapproved_posts()

    return jsonify(unapproved_posts), 200

@posts_bp.route('/approve', methods=['POST'])
@cross_origin()
def approve_post():
    data = request.json  # Parse JSON body
    print("Received data:", data)  # Debug log
    post_id = data.get('post_id')  # Extract post_id from the body
    print("Extracted post_id:", post_id)  # Debug log
    post = PostService.get_post_by_id(post_id)
    print(post)
    if post:
        PostService.approve_post(post_id)
        response = {'message': 'Post approved'}
        return jsonify(response), 200
    return jsonify({'message': 'Post not found'}), 404

@posts_bp.route('/reject', methods=['POST'])
@cross_origin()
def reject_post():
    data = request.json  # Parse JSON body
    print("Received data:", data)  # Debug log
    post_id = data.get('post_id')  # Extract post_id from the body
    print("Extracted post_id:", post_id)  # Debug log

    if not post_id:
        return jsonify({'message': 'Post ID is required'}), 400

    post = PostService.get_post_by_id(post_id)
    if post:
        PostService.delete_post(post_id)
        response = {'message': 'Post rejected'}
        return jsonify(response), 200

    return jsonify({'message': 'Post not found'}), 404



