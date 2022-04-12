import json

class CommentsDAO:

    def __init__(self, path: str) -> None:
        """Path to data file needs to be submitted when creating dao object """
        self.path = path

    def get_data(self) -> list:
        """Create a list of all comments from a json file"""

        with open(self.path, mode='r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_comments_by_post_id(self, post_id: int) -> list:
        """Get all comments post which contain specific word from a json file

        Arguments:
        post_id -- id of the associated post
        """
        comments = self.get_data()
        comments_found = [comment for comment in comments if comment['post_id'] == post_id]
        return comments_found
