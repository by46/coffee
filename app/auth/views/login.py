# -*- coding:utf-8 -*-

from flask import current_app
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from flask_principal import AnonymousIdentity
from flask_principal import Identity
from flask_principal import identity_changed

from app.auth import auth
from app.auth.forms import LoginForm
from app.models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(request.args.get('next') or url_for('portal.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name=form.username.data).first()
        password = form.password.data
        if user is not None and user.verify_password(password):
            login_user(user)
            identity_changed.send(
                current_app._get_current_object(),
                identity=Identity(user.id))
            return redirect(request.args.get('next') or url_for('portal.index'))
        else:
            flash(u'用户名或密码错误。')

    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    identity_changed.send(
        current_app._get_current_object(),
        identity=AnonymousIdentity())
    flash(u'登出系统')
    return redirect(url_for('auth.login'))
