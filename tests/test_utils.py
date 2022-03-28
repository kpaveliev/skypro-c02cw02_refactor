import pytest
import os, sys

path = os.path.abspath('.')
sys.path.insert(1, path)

from utils import *
from app import POSTS, COMMENTS, BOOKMARKS


# Define tests for functions
def test_get_data():
    """Check if json loads correctly"""
    posts = get_data(POSTS)
    assert len(posts) == 8, "Ошибка загрузки файла"
    assert posts[0]['poster_name'] == 'leo', "Ошибка загрузки файла"

def test_get_data_exception():
    """Check if FileNotFoundError is raised correctly"""
    with pytest.raises(FileNotFoundError):
        get_data('some.json')

def test_get_posts_by_user():
    """Check if posts by user are loaded correctly"""
    posts_found = get_posts_by_user(POSTS, 'larry')
    assert len(posts_found) == 2, "Ошибка поиска по пользователю"
    assert posts_found[0]['poster_name'] == 'larry', "Ошибка поиска по пользователю"

def test_get_post_by_id():
    """Check if posts by id are found correctly"""
    post = get_post_by_id(POSTS, 1)
    assert len(post) == 7, "Ошибка поиска по id"
    assert post['pk'] == 1, "Ошибка поиска по id"

def test_get_posts_for_word():
    """Check if posts are found correctly"""
    posts = get_posts_for_word(POSTS, 'вышел')
    assert len(posts) == 1, "Ошибка поиска по слову"
    assert posts[0]['pk'] == 2, "Ошибка поиска по id"

def test_get_comments_by_id():
    """Check if comments are found correctly by post id"""
    assert len(get_comments_by_post_id(COMMENTS, 2)) == 4, "Ошибка загрузки комментариев"
