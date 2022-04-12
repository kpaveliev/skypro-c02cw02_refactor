import json

class PostsDAO:

    def __init__(self, path: str) -> None:
        """Path to data file needs to be submittes when creating dao object """
        self.path = path

    def get_data(self) -> list:
        """Create a list of all posts from a json file"""

        with open(self.path, mode='r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def get_posts_by_user(self, user_name: str) -> list:
        """Create list of posts by specific user from a json file

        Arguments:
        username -- name of a user
        """
        posts = self.get_data()
        posts_found = [post for post in posts if user_name in post['poster_name']]
        return posts_found

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

    def format_post_tags(self, post: dict) -> dict:
        """Replace post tags in the post content with html links

        Arguments:
        post -- post where tags should be replaced
        """
        content = post['content'].split(' ')
        content_tagged = []

        for word in content:
            if word[0] == '#':
                content_tagged.append(f'<a href="/tag/{word[1:]}" class="item__tag">{word}</a>')
            else:
                content_tagged.append(word)

        post['content'] = ' '.join(content_tagged)

        return post

    def get_posts_for_word(self, searched_word: str) -> list:
        """Get all posts which contain specific word from a json file

        Arguments:
        searched_word -- word submitted for search
        """
        posts = self.get_data()
        posts_found = [post for post in posts if searched_word.lower() in post['content'].lower()]
        return posts_found
