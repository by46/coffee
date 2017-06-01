from flask import render_template
from flask_login import login_required
from flask_menu import register_menu

from app.portal import portal


@portal.route('/profile2')
@register_menu(portal, '.profile', 'Profile')
@login_required
def profile2():
    return render_template('portal/profile.html')


@portal.route('/profile')
@register_menu(portal, '.profile.info', 'Basic info')
@login_required
def profile():
    return render_template('portal/profile.html')
