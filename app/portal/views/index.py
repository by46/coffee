from  flask import render_template
from flask_login import login_required

from app import default_permission
from app.portal import portal


@portal.route('/')
@login_required
@default_permission.require(http_exception=403)
def index():
    return render_template('portal/index.html')
