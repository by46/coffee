from flask import render_template

from app.main import main


@main.route('/vue')
def vue():
    return render_template('index.html')
