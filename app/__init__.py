"""demo

"""

from flask import Flask
from flask_assets import Environment
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt import JWT
from flask_login import LoginManager
from flask_login import current_user
from flask_menu import Menu
from flask_principal import Permission
from flask_principal import Principal
from flask_principal import RoleNeed
from flask_principal import UserNeed
from flask_principal import identity_loaded
from flask_sqlalchemy import SQLAlchemy

from flask_kits.routing import KitRule
from flask_pygments import Pygments
from flask_upload import Upload
from .assets import register_bundle
from .utils import config_menu

Flask.url_rule_class = KitRule

__version__ = '0.0.1'
__author__ = 'Recipe'

principals = Principal()
login_manager = LoginManager()
cors = CORS()
db = SQLAlchemy()
uploader = Upload()
jwt = JWT()
pygments = Pygments()
assets = Environment()
bcrypt = Bcrypt()
register_bundle(assets)
menu = Menu()

admin_permission = Permission(RoleNeed('admin'))
default_permission = Permission(RoleNeed('default'))


def create_app(config_name):
    app = Flask(__name__, static_url_path='/coffee/static')
    app.config.from_object('config.default')
    app.config.from_object('config.{0}'.format(config_name.lower()))
    app.config['VERSION'] = __version__

    login_manager.init_app(app)
    cors.init_app(app)
    db.init_app(app)
    uploader.init_app(app)
    # jwt.init_app(app)
    pygments.init_app(app)
    assets.init_app(app)
    bcrypt.init_app(app)
    principals.init_app(app)
    principals.init_app(app)
    menu.init_app(app)

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        """
        
        :param sender: 
        :param identity: 
        :return: 
        """
        identity.user = current_user

        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.name))

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .h5 import h5 as h5_blueprint
    from .portal import portal as portal_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(h5_blueprint)
    app.register_blueprint(portal_blueprint)

    config_menu(app, [
        {'name': 'profile', 'text': 'Home', 'role': 'default', 'order': 1},
        {'name': 'log', 'text': 'Log', 'order': 2},
        {'name': 'project', 'text': 'Project', 'role': 'admin', 'order': 4},
        {'name': 'budget', 'text': 'Budget', 'role': 'default', 'order': 3},
    ])
    return app
