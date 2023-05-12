from flask_app import app
from flask import render_template, redirect, request, url_for, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.models import post

@app.route("/post")
def display_post():
    if session.get('logged_in') == True:
        all_posts = post.Post.get_all()
        return render_template("wall.html", all_posts = all_posts)
    return "You are not logged in"

@app.route("/post", methods=["POST"])
def user_post():
    data = {
        "content" : request.form["user_post"],
        "user_id" : session["id"]
    }
    post.Post.create(data)
    return redirect("/post")

@app.route("/delete_post", methods=["POST"])
def delete_post():
    data = {
        "post_id" : request.form["post_id"]
    }
    print("Here is the data")
    print(data)
    post.Post.delete_post(data)
    return redirect("/post")