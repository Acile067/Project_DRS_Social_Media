from flask import Blueprint, request, jsonify
from app.services.post_service import PostService

posts_bp = Blueprint('posts_bp', __name__)

@posts_bp.route('/getallposts', methods=["GET"])
def get_all_posts():
    response, status = PostService.get_all_posts()
    return jsonify(response), status

@posts_bp.route('/getalluserposts', methods=['GET'])
def get_all_posts_for_user():
    username = request.args.get('username')
    response, status = PostService.get_all_posts_for_user(username)
    return jsonify(response), status

@posts_bp.route('/createpost', methods=['POST'])
def create():
    data = request.json
    response, status = PostService.create_post(data.get('post_id'),data.get('username'),data.get('txt'),
                                               data.get('image_path'),data.get('approved'))
    return jsonify(response), status

@posts_bp.route('/editpost', methods=['GET, POST'])
def edit(post_data):
    post_id = post_data.get('post_id')
    if request.method == 'GET':
        response, status = PostService.get_post_by_id(post_id)
        return {"data": response}, status

    elif request.method == 'POST':
        data = request.json
        response, status = PostService.edit_post(data.get('post_id'),data.get('username'),data.get('txt'),
                                               data.get('image_path'),data.get('approved'))
        return jsonify(response), status




