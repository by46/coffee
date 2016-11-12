from flask import Blueprint
from flask_restful import Api
from flask_restful_swagger import swagger

url_prefix = '/coffee'
main = Blueprint('main', __name__, url_prefix=url_prefix)

api = swagger.docs(Api(main), apiVersion="1.0")

from . import views
