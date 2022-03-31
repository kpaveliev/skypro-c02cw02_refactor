import pytest
import os
import sys
path = os.path.abspath('.')
sys.path.insert(1, path)
from utils import get_data, get_post_by_id, get_comments_by_post_id, get_posts_by_user, get_posts_for_word
from app import POSTS, COMMENTS


# Define tests for functions
def test_get_data():
    """Check if json loads correctly"""
    posts = get_data(POSTS)
    keys_to_check = ('poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk')
    assert isinstance(posts, list), "Ошибка загрузки файла: полученный объект не является списком"
    assert tuple(posts[0].keys()) == keys_to_check, "Ошибка загрузки файла: элементы списка не содержат нужные ключи"


def test_get_data_exception():
    """Check if FileNotFoundError is raised correctly"""
    with pytest.raises(FileNotFoundError):
        get_data('some.json')


def test_get_posts_by_user():
    """Check if posts by user are loaded correctly"""
    posts = get_posts_by_user(POSTS, 'larry')
    keys_to_check = ('poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk')
    assert isinstance(posts, list), "Ошибка поиска по пользователю: полученный объект не является списком"
    assert tuple(posts[0].keys()) == keys_to_check, "Ошибка поиска по пользователю: элементы списка не содержат нужные ключи"


def test_get_post_by_id():
    """Check if posts by id are found correctly"""
    post = get_post_by_id(POSTS, 1)
    keys_to_check = ('poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk')
    assert isinstance(post, dict), "Ошибка поиска по id: полученный объект не явлется словарем"
    assert tuple(post.keys()) == keys_to_check, "Ошибка поиска по id: объект не содержит нужных ключей"


def test_get_posts_for_word():
    """Check if posts are found correctly"""
    posts = get_posts_for_word(POSTS, 'вышел')
    keys_to_check = ('poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk')
    assert isinstance(posts, list), "Ошибка поиска по слову: полученный объект не является списком"
    assert tuple(posts[0].keys()) == keys_to_check, "Ошибка поиска по слову: элементы списка не содержат нужные ключи"


def test_get_comments_by_id():
    """Check if comments are found correctly by post id"""
    comments = get_comments_by_post_id(COMMENTS, 2)
    keys_to_check = ('post_id', 'commenter_name', 'comment', 'pk')
    assert isinstance(comments, list), "Ошибка загрузки комментариев: полученный объект не является списком"
    assert tuple(comments[0].keys()) == keys_to_check, "Ошибка загрузки комментариев: элементы списка не содержат нужные ключи"
