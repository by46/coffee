from flask import Blueprint

from app.utils import make_url_prefix

portal = Blueprint('portal', __name__, url_prefix=make_url_prefix('portal'))
from . import views
