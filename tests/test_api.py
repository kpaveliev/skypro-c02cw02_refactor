# import pytest
# import os, sys
#
# path = os.path.abspath('.')
# sys.path.insert(1, path)
#
# from app import POSTS, COMMENTS
# from api.api import api_posts
#
# # Define tests for functions
# def test_api_posts():
#     """Check if json loads correctly"""
#     result = api_posts()
#     assert isinstance(result, list) == 8, "Ошибка загрузки файла"
