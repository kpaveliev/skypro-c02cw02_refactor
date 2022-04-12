import pytest

@pytest.fixture()
def posts_keys():
    return {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}