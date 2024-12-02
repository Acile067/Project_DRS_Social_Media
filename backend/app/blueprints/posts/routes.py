from flask import Blueprint, request, jsonify
from app.blueprints.auth.auth import token_required
from app.services.post_service import PostService
from flask_cors import cross_origin

posts_bp = Blueprint('posts_bp', __name__)

@posts_bp.route('/getallposts', methods=["GET"])
@cross_origin()
@token_required
def get_all_posts(user_data):
    response, status = PostService.get_all_posts()
    return jsonify(response), status

@posts_bp.route('/approvedpostsforuser', methods=['GET'])
@cross_origin()
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
    txt = request.form.get('txt')
    image = request.files.get('image')

    response, status = PostService.create_post_with_image(current_user_id, txt, image)
    return jsonify(response), status

@posts_bp.route('/editpost', methods=['GET', 'POST'])
@cross_origin()
@token_required
def edit(user_data):
    if request.method == 'GET':
        post_id = request.args.get('post_id')
        response, status = PostService.get_post_by_id(post_id)
        return {"data": response}, status

    elif request.method == 'POST':
        data = request.json
        response, status = PostService.edit_post(data.get('post_id'),data.get('username'),data.get('txt'),
                                               data.get('image_path'),data.get('approved'))
        return jsonify(response), status

@posts_bp.route('/delete', methods=['POST'])
@cross_origin()
@token_required
def delete_post(user_data):
    data = request.json  # Parse JSON body
    post_id = data.get('post_id')  # Extract post_id from the body

    if not post_id:
        return jsonify({'message': 'Post ID is required'}), 400

    post = PostService.get_post_by_id(post_id)
    if post:
        PostService.delete_post(post_id)
        response = {'message': 'Post deleted successfully'}
        return jsonify(response), 200

    return jsonify({'message': 'Post not found'}), 404

@posts_bp.route('/unapproved', methods=['GET'])
@cross_origin()
@token_required
def get_unapproved_posts(user_data):
    unapproved_posts = PostService.get_unapproved_posts()

    return jsonify(unapproved_posts), 200

@posts_bp.route('/friendsposts', methods=['GET'])
@cross_origin()
@token_required
def get_friends_posts_posts(user_data):
    current_user_id = user_data.get('user_id')
    response, status = PostService.get_all_friends_posts_for_user(current_user_id)
    return jsonify(response), status


@posts_bp.route('/approve', methods=['POST'])
@cross_origin()
@token_required
def approve_post(user_data):
    current_user_id = user_data.get('user_id')
    data = request.json  # Parse JSON body
    post_id = data.get('post_id')  # Extract post_id from the body
    post = PostService.get_post_by_id(post_id)
    if post:
        PostService.approve_post(post_id, current_user_id)
        response = {'message': 'Post approved'}
        return jsonify(response), 200
    return jsonify({'message': 'Post not found'}), 404

@posts_bp.route('/reject', methods=['POST'])
@cross_origin()
@token_required
def reject_post(user_data):
    current_user_id = user_data.get('user_id')
    data = request.json  # Parse JSON body
    post_id = data.get('post_id')  # Extract post_id from the body

    if not post_id:
        return jsonify({'message': 'Post ID is required'}), 400

    post = PostService.get_post_by_id(post_id)
    if post:
        PostService.reject_post(post_id,current_user_id)
        response = {'message': 'Post rejected'}
        return jsonify(response), 200

    return jsonify({'message': 'Post not found'}), 404