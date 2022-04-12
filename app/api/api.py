from flask import Blueprint, jsonify
from app.main.dao.posts_dao import PostsDAO

# Create a Blueprint object
api_blueprint = Blueprint('api_blueprint', __name__, url_prefix='/api')
posts_dao = PostsDAO('data/data.json')

# Create views
@api_blueprint.route("/posts/")
def api_posts():
    """Return posts as a json object"""
    posts = posts_dao.get_data()
    return jsonify(posts), {'Content-type': 'application/json; charset=utf-8'}


@api_blueprint.route("/posts/<int:post_id>")
def api_post_by_id(post_id):
    """Return specified post as a json object"""
    post = posts_dao.get_post_by_id(post_id)
    return jsonify(post), {'Content-type': 'application/json; charset=utf-8'}
