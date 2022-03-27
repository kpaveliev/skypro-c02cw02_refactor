from flask import Flask, render_template
from utils import *

# Key variables
POSTS = 'data/data.json'
COMMENTS = 'data/comments.json'

# Initiate Flask app
app = Flask(__name__, static_folder='static')
app.debug = True

@app.route("/")
def main():
    posts = get_data(POSTS)
    return render_template('index.html', posts=posts)


@app.route("/posts/<int:post_id>")
def post_by_id(post_id):
    post = get_post_by_id(POSTS, post_id)
    comments = get_comments_by_post_id(COMMENTS, post_id)
    return render_template('post.html', post=post, comments=comments)

# Add a route to display images from uploads folder
# @app.route("/resources/uploads/<path:path>")
# def static_dir(path):
#     return send_from_directory("/resources/uploads/", path)

if __name__ == '__main__':
    app.run()