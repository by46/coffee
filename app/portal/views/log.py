# -:- coding:utf8 -:-
from flask import g
from flask import render_template
from flask_login import login_required

from app.portal import portal
from app.utils import register_menu_ex


@portal.route('/log')
@register_menu_ex(portal, '.log.system_log', "日志", roles=['default'])
@login_required
def log():
    print(g.identity)
    return render_template('portal/log.html')
