from flask import render_template

from app.google import router


@router.route("/")
def home():
    return render_template("google/index.html")
