from flask import Blueprint

url_prefix = '/coffee/h5'

h5 = Blueprint('h5', __name__, url_prefix=url_prefix)

from . import views
