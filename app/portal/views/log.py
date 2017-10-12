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


@portal.route('/logs')
@login_required
def logs():
    print(g.identity)
    return render_template('portal/logs.html')


@portal.route('/log_detail')
@login_required
def log_detail():
    print(g.identity)
    return render_template('portal/log_detail.html')
