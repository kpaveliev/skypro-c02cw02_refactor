from flask import Blueprint, jsonify
from utils import *

# Key variables
POSTS = 'data/data.json'

# Create a Blueprint object
api_blueprint = Blueprint('api_blueprint', __name__)

# Create views
@api_blueprint.route("/posts")
def api_posts():
    """Return posts as json"""
    posts = get_data(POSTS)
    return jsonify(posts)


@api_blueprint.route("/posts/<int:post_id>")
def api_post_by_id(post_id):
    """Return post as json"""
    post = get_post_by_id(POSTS, post_id)
    return jsonify(post)
