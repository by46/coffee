"""demo

"""

from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT
from flask_login import LoginManager
from flask_neglog import Log
from flask_sqlalchemy import SQLAlchemy

from flask_upload import Upload

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

log_manager = Log()
login_manager = LoginManager()
cors = CORS()
db = SQLAlchemy()
uploader = Upload()
jwt = JWT()


def create_app(config_name):
    app = Flask(__name__, static_url_path='/coffee/static')
    app.config.from_object('config.default')
    app.config.from_object('config.{0}'.format(config_name.lower()))
    app.config['VERSION'] = __version__

    log_manager.init_app(app)
    login_manager.init_app(app)
    cors.init_app(app)
    db.init_app(app)
    uploader.init_app(app)
    # jwt.init_app(app)
    from werkzeug.exceptions import NotFound
    from werkzeug.exceptions import InternalServerError
    @app.errorhandler(NotFound)
    def handle_bad_request(e):
        return 'bad request'

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    return app
