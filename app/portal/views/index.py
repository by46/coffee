from flask import render_template
from flask_login import login_required
from flask_menu import register_menu

from app import default_permission
from app.portal import portal


@portal.route('/')
@register_menu(portal, '.index', 'Home', order=1)
@login_required
@default_permission.require(http_exception=403)
def index():
    return render_template('portal/index.html')
