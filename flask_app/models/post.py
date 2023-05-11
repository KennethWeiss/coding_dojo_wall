from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

class Post:
    db = "coding_dojo_wall"
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None

    @classmethod
    def create(cls,data):
        query = """INSERT INTO posts (content, user_id) 
                VALUES (%(content)s, %(user_id)s);"""
        results = connectToMySQL(cls.db).query_db(query,data)
        return results