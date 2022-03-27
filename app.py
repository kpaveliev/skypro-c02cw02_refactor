from flask import Flask, render_template, request, redirect
from utils import *

# Key variables
POSTS = 'data/data.json'
COMMENTS = 'data/comments.json'
BOOKMARKS = 'data/bookmarks.json'

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
    tagged_post = format_post_tags(post)
    comments = get_comments_by_post_id(COMMENTS, post_id)
    return render_template('post.html', post=tagged_post, comments=comments)


@app.route("/users/<user_name>")
def posts_by_user(user_name):
    posts = get_posts_by_user(POSTS, user_name)
    return render_template('user-feed.html', posts=posts, user_name=user_name)


@app.route("/tag/<tag_name>")
def posts_by_tag(tag_name):
    posts_found = get_posts_for_word(POSTS, f'#{tag_name}')
    return render_template('tag.html', posts=posts_found, tag_name=tag_name.capitalize())


@app.route("/search")
def posts_search():
    searched_word = request.args.get('s')
    posts_found = get_posts_for_word(POSTS, searched_word)
    return render_template('search.html', posts=posts_found)


@app.route("/bookmarks/add/<int:post_id>")
def bookmarks_add(post_id):
    # data = get_data(BOOKMARKS)
    data = []
    data.append(get_post_by_id(POSTS, post_id))
    write_data(BOOKMARKS, data)
    return redirect("/", code = 302)

@app.route("/bookmarks")
def bookmarks():
    posts = get_data(BOOKMARKS)
    return render_template('bookmarks.html', posts=posts)

# Add a route to display images from uploads folder
# @app.route("/resources/uploads/<path:path>")
# def static_dir(path):
#     return send_from_directory("/resources/uploads/", path)

if __name__ == '__main__':
    app.run()