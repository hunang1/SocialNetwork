# user.py

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.friends = []

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def add_friend(self, friend):
        self.friends.append(friend)

    def get_friends(self):
        return self.friends
