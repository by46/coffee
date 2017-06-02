from flask import render_template
from flask_login import login_required
from flask_menu import register_menu
from flask import g
from app.portal import portal


@portal.route('/log')
@register_menu(portal, '.log.system_log', "日志")
@login_required
def log():
    print(g.identity)
    return render_template('portal/log.html')
