from flask_app import app
from flask import render_template, redirect, request, url_for, session, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# from flask_app.models import post

@app.route("/post")
def post():
    return "Posted"