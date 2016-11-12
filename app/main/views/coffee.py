from flask_restful import Resource
from flask_restful import marshal_with
from flask_restful_swagger import swagger

from app.main import api
from app.main.meta import filter_params
from app.main.serializer import CoffeeResource
from app.models import Coffee


class CoffeeApi(Resource):
    @swagger.operation(notes="Coffee list", parameters=filter_params())
    @marshal_with(CoffeeResource)
    def get(self):
        return Coffee.query.paginate().items


api.add_resource(CoffeeApi, '/coffees')
