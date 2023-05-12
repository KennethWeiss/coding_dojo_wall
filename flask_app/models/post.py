from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Post:
    db = "coding_dojo_wall"
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = None

    @classmethod
    def create(cls,data):
        query = """INSERT INTO posts (content, user_id) 
                VALUES (%(content)s, %(user_id)s);"""
        results = connectToMySQL(cls.db).query_db(query,data)
        return results
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts ORDER BY posts.created_at desc;"
        results = connectToMySQL(cls.db).query_db(query)
        all_posts = []
        for post in results:
            all_posts.append(cls(post))
        return all_posts
    
    @classmethod
    def delete_post(cls,data):
        query = "DELETE FROM posts where id = %(post_id)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @staticmethod
    def valid_post(post_content):
        is_valid = True
        if len(post_content) < 1:
            is_valid = False
            flash("Post cannot be empty", "post")
        return is_valid
