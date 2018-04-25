from flask import Blueprint

from app.utils import make_url_prefix

router = Blueprint('google', __name__, url_prefix=make_url_prefix('google'))
from . import views
