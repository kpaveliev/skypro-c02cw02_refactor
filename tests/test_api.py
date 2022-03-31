import pytest
import os
import sys
path = os.path.abspath('.')
sys.path.insert(1, path)
from app import app

# Define tests for view functions
def test_api_posts():
    """Check if json with all the posts loads correctly"""
    response = app.test_client().get('/api/posts/')
    posts = response.json
    keys_to_check = ('poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk')
    assert isinstance(posts, list), "Ошибка API (загрузка постов): выгружается не список"
    assert sorted(tuple(posts[0].keys())) == sorted(keys_to_check), "Ошибка API (загрузка постов): нет нужных ключей"


def test_api_post_by_id():
    """Check if json with specified post loads correctly"""
    response = app.test_client().get('/api/posts/1')
    post = response.json
    keys_to_check = ('poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk')
    assert isinstance(post, dict), "Ошибка API (загрузка поста по ID): выгружается не словарь"
    assert sorted(tuple(post.keys())) == sorted(keys_to_check), "Ошибка API (загрузка поста по ID): нет нужных ключей"
