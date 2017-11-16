from flask import render_template

from app.portal import portal


@portal.route("/xss/demo", methods=['GET'])
def xss_demo():
    return render_template('portal/xss_demo.html', name='benjamin\'')
