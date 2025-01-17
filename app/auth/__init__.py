from flask import Blueprint

from app.utils import make_url_prefix

auth = Blueprint('auth', __name__, url_prefix=make_url_prefix('auth'))

from . import views
