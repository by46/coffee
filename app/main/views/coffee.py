from datetime import datetime

from flask_login import login_required
from flask_restful import Resource
from flask_restful import marshal_with
from flask_restful import reqparse
from flask_restful_swagger import swagger

from app import db
from app.decorators import manager_required
from app.main import api
from app.main.meta import CoffeeModel
from app.main.meta import filter_params
from app.main.serializer import CoffeeResource
from app.models import Coffee
from .resource import BusinessResource


class CoffeeApi(BusinessResource):
    @swagger.operation(notes="Coffee list", parameters=filter_params())
    @marshal_with(CoffeeResource)
    def get(self):
        return Coffee.query.filter_by(vendor_id=1).paginate().items

    @swagger.operation(notes="New Coffee List",
                       parameters=[{
                           'name': 'coffee',
                           'description': 'new coffer information',
                           'dataType': CoffeeModel.__name__,
                           'paramType': 'body'
                       }])
    @marshal_with(CoffeeResource)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', str, help="coffer's name")
        parser.add_argument('on_sale_date', type=lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S'))
        args = parser.parse_args()
        coffee = Coffee(name=args.name, on_sale_date=args.on_sale_date, vendor_id=1)
        db.session.add(coffee)
        db.session.commit()
        return coffee


api.add_resource(CoffeeApi, '/coffees')


class Coffee2Api(Resource):
    @login_required
    @manager_required
    @swagger.operation(notes="Coffee list", parameters=filter_params())
    @marshal_with(CoffeeResource)
    def get(self):
        return Coffee.query.paginate().items


api.add_resource(Coffee2Api, '/coffees2')
