# social_network.py

from user import User
from post import Post

class SocialNetwork:
    def __init__(self):
        self.users = []
        self.posts = []

    def create_user(self, username, email):
        user = User(username, email)
        self.users.append(user)
        return user

    def create_post(self, content, author):
        post = Post(content, author)
        self.posts.append(post)
        return post

    def add_friend(self, user, friend):
        if user in self.users and friend in self.users:
            user.add_friend(friend)
            friend.add_friend(user)
        else:
            raise ValueError("Invalid user or friend")

    def add_comment(self, post, comment):
        if post in self.posts:
            post.add_comment(comment)
        else:
            raise ValueError("Invalid post")

    def get_users(self):
        return self.users

    def get_posts(self):
        return self.posts
