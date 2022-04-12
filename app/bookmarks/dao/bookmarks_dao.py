import json

class BookmarksDAO:

    def __init__(self, path: str) -> None:
        """Path to data file needs to be submitted when creating dao object """
        self.path = path

    def get_data(self) -> list:
        """Create a list of all bookmarks from a json file"""

        with open(self.path, mode='r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def write_data(self, data: list) -> None:
        """Save data to a json file

        Arguments:
        data - data to append
        """
        with open(self.path, mode='w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def get_post_by_id(self, post_id: int) -> dict:
        """Get post with the specified id from a json file

        Arguments:
        post_id -- id of the post
        """
        posts = self.get_data()
        post_found = None

        for post in posts:
            if post['pk'] == post_id:
                post_found = post

        return post_found
