from flask import render_template
from app.auth import auth

@auth.route('/demo1')
def demo1():
    return render_template('auth/demo1.html')