from flask import Blueprint

auth = Blueprint('auth', __name__, url_prefix='/coffee/auth')

from . import views

