# 

class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.comments = []

    def get_content(self):
        return self.content

    def get_author(self):
        return self.author

    def add_comment(self, comment):
        self.comments.append(comment)

    def get_comments(self):
        return self.comments
