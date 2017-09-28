from flask import Blueprint
from flask_restful import Api
from flask_restful_swagger import swagger

from app.utils import make_url_prefix

api = Blueprint('api', __name__, url_prefix=make_url_prefix('api/v1'))
restful_api = swagger.docs(Api(api), apiVersion='1.0')

from . import views
