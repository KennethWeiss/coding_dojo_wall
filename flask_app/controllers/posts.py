from flask_app import app
from flask import render_template, redirect, request, url_for, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import post

@app.route("/post")
def display_post():
    all_posts = post.Post.get_all()
    print("Here are the posts")
    print(all_posts)
    return redirect("/success")

@app.route("/post", methods=["POST"])
def user_post():
    data = {
        "content" : request.form["user_post"],
        "user_id" : session["id"]
    }
    post.Post.create(data)
    return redirect("/post")