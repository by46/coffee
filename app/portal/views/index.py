from  flask import render_template

from app.portal import portal


@portal.route('/')
def index():
    return render_template('portal/index.html')
