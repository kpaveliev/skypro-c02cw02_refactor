from flask import Blueprint, current_app, request, redirect, render_template
from .dao.bookmarks_dao import BookmarksDAO
from app.main.dao.posts_dao import PostsDAO


# Create a Blueprint object and DAO
bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__,
                                url_prefix='/bookmarks', template_folder='templates')
bookmarks_dao = BookmarksDAO('data/bookmarks.json')
posts_dao = PostsDAO('data/data.json')

# Create views
@bookmarks_blueprint.route("/")
def bookmarks():
    """Page with all posts added to bookmarks"""
    posts = bookmarks_dao.get_data()
    return render_template('bookmarks.html', posts=posts)


@bookmarks_blueprint.route("/add/<int:post_id>")
def bookmarks_add(post_id):
    """Add the post to bookmarks"""
    try:
        bookmarks = bookmarks_dao.get_data()
    except JSONDecodeError:
        # If bookmarks.json is empty, declare empty variable
        bookmarks = []
    else:
        # Add post to the bookmarks if it isn't added already
        post_check = bookmarks_dao.get_post_by_id(post_id)
        if post_check is None:
            post_to_add = posts_dao.get_post_by_id(post_id)
            bookmarks.append(post_to_add)
            bookmarks_dao.write_data(bookmarks)
    finally:
        # Get page url to redirect to the same page
        url_redirect = request.referrer
        return redirect(url_redirect, code=302)


@bookmarks_blueprint.route("/remove/<int:post_id>")
def bookmarks_remove(post_id):
    """Remove the post from the bookmarks"""
    # Get post to remove
    post_to_remove = bookmarks_dao.get_post_by_id(post_id)
    # Remove post from the bookmarks
    bookmarks = bookmarks_dao.get_data()
    bookmarks.remove(post_to_remove)
    bookmarks_dao.write_data(bookmarks)
    # Get page url to redirect to the same page
    url_redirect = request.referrer
    return redirect(url_redirect, code=302)