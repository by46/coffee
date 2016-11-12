"""demo

"""

from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_neglog import Log
from flask_sqlalchemy import SQLAlchemy

__version__ = '0.0.1'
__author__ = 'Recipe'

log_manager = Log()
login_manager = LoginManager()
cors = CORS()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, static_url_path='/coffee/static')
    app.config.from_object('config.default')
    app.config.from_object('config.{0}'.format(config_name.lower()))
    app.config['VERSION'] = __version__

    log_manager.init_app(app)
    login_manager.init_app(app)
    cors.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
