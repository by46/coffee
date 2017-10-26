from flask import render_template
from flask_login import login_required

from app import default_permission
from app.portal import portal
from app.utils import register_menu_ex


@portal.route('/')
@register_menu_ex(portal, '.index', 'Home', order=1)
@login_required
@default_permission.require(http_exception=403)
def index():
    return render_template('portal/index.html')


@portal.route('/index.json')
def json():
    return render_template('portal/index.json'), 200, {'Content-Type': 'Application/json'}
