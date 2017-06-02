from flask import render_template
from flask_login import login_required
from flask_menu import register_menu

from app.portal import portal


@portal.route('/profile')
@register_menu(portal, '.profile.info', 'Basic info')
@login_required
def profile():
    return render_template('portal/profile.html')
