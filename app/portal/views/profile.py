from flask import render_template
from flask_login import login_required

from app.portal import portal
from app.utils import register_menu_ex


@portal.route('/profile')
@register_menu_ex(portal, '.profile.info', 'Basic info', roles=['default'])
@login_required
def profile():
    return render_template('portal/profile.html')
