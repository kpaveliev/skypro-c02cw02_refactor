from flask import Blueprint, jsonify, current_app
from utils import get_data, get_post_by_id

# Create a Blueprint object
api_blueprint = Blueprint('api_blueprint', __name__)


# Create views
@api_blueprint.route("/posts/")
def api_posts():
    """Return posts as json"""
    POSTS = current_app.config.get('POSTS')
    posts = get_data(POSTS)
    return jsonify(posts), {'Content-type': 'application/json; charset=utf-8'}


@api_blueprint.route("/posts/<int:post_id>")
def api_post_by_id(post_id):
    """Return specified post as json"""
    POSTS = current_app.config.get('POSTS')
    post = get_post_by_id(POSTS, post_id)
    return jsonify(post), {'Content-type': 'application/json; charset=utf-8'}
