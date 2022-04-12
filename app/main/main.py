from flask import Blueprint, render_template, request, current_app
from .dao.posts_dao import PostsDAO
from .dao.comments_dao import CommentsDAO
from app.bookmarks.dao.bookmarks_dao import BookmarksDAO

# Create a Blueprint object and dao
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
posts_dao = PostsDAO('data/data.json')
comments_dao = CommentsDAO('data/comments.json')
bookmarks_dao = BookmarksDAO('data/bookmarks.json')

# Create post views
@main_blueprint.route("/")
def main():
    """Main page with all the posts"""
    posts = posts_dao.get_data()
    bookmarks = bookmarks_dao.get_data()
    return render_template('index.html', posts=posts, bookmarks=bookmarks)


@main_blueprint.route("/posts/<int:post_id>")
def post_by_id(post_id):
    """Page with a specific post"""
    post = posts_dao.get_post_by_id(post_id)
    tagged_post = posts_dao.format_post_tags(post)
    comments = comments_dao.get_comments_by_post_id(post_id)
    bookmarks = bookmarks_dao.get_data()
    return render_template('post.html', post=tagged_post, bookmarks=bookmarks, comments=comments)


# Views by user, tag, search by word
@main_blueprint.route("/users/<user_name>")
def posts_by_user(user_name):
    """Page with all the posts of the user"""
    posts = posts_dao.get_posts_by_user(user_name)
    bookmarks = bookmarks_dao.get_data()
    return render_template('user-feed.html', posts=posts, bookmarks=bookmarks,
                           user_name=user_name)


@main_blueprint.route("/tag/<tag_name>")
def posts_by_tag(tag_name):
    """Page with all the posts containing the tag"""
    posts_found = posts_dao.get_posts_for_word(f'#{tag_name}')
    bookmarks = bookmarks_dao.get_data()
    return render_template('tag.html', posts=posts_found,
                           bookmarks=bookmarks, tag_name=tag_name.capitalize())


@main_blueprint.route("/search")
def posts_search():
    """Page with all the posts containing searched word or phrase"""
    try:
        searched_word = request.args.get('s')
        posts_found = posts_dao.get_posts_for_word(searched_word)
        bookmarks = bookmarks_dao.get_data()
    except:
        # Allow opening without arguments
        return render_template('search.html', posts=[], bookmarks=[])
    else:
        return render_template('search.html', posts=posts_found, bookmarks=bookmarks)
