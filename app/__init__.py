"""demo

"""

from flask import Flask
from flask_assets import Environment
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_jwt import JWT
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from flask_kits.routing import KitRule
from flask_pygments import Pygments
from flask_upload import Upload
from .assets import register_bundle

Flask.url_rule_class = KitRule

__version__ = '0.0.1'
__author__ = 'Recipe'


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id


users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

login_manager = LoginManager()
cors = CORS()
db = SQLAlchemy()
uploader = Upload()
jwt = JWT()
pygments = Pygments()
assets = Environment()
bcrypt = Bcrypt()

register_bundle(assets)


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

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .h5 import h5 as h5_blueprint
    from .portal import portal as portal_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(h5_blueprint)
    app.register_blueprint(portal_blueprint)

    return app
