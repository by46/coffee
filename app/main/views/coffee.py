from dateutil.parser import parse
from flask_login import login_required
from flask_restful import Resource
from flask_restful import marshal_with
from flask_restful import reqparse
from flask_restful_swagger import swagger
from sqlalchemy import func

from app import db
from app.decorators import manager_required
from app.main import api
from app.main.meta import CoffeeModel
from app.main.meta import filter_params
from app.main.serializer import CoffeeResource
from app.models import Coffee
from app.models import Feedback
from flask_kits.restful import Paginate
from .resource import BusinessResource


def custom_datetime(value, name):
    return parse(value)


def set_feedback_count(record):
    if not isinstance(record, tuple):
        return record
    item, count = record
    item.feedback_count = count
    return item


class CoffeeApi(BusinessResource):
    @swagger.operation(notes="Coffee list", parameters=filter_params())
    @Paginate(CoffeeResource, item_builder=set_feedback_count)
    def get(self):
        db.session.query(Coffee, func.count(Feedback.id)).outerjoin(Feedback, Coffee.id == Feedback.coffee_id).group_by(
            Coffee.id).all()
        print db.session.query(Coffee.name, Coffee.id).first()
        print db.session.query(Coffee).order_by(Coffee.name)[2:5]
        print db.session.query(Coffee).order_by(Coffee.name).limit(2).all()
        print 'count:', db.session.query(func.sum(Coffee.id)).scalar()
        print 'count & sum', db.session.query(func.count(Coffee.id), func.sum(Coffee.id)).first()
        result = db.session.query(func.count(Coffee.id).label('count_1'), func.sum(Coffee.id).label('sum_1')).first()
        print 'count & sum', result.keys(), result.count_1, result.sum_1

        query = db.session.query(Coffee, func.count(Feedback.id))
        query.outerjoin(Feedback, Coffee.id == Feedback.coffee_id)
        query.group_by(Coffee.id)
        # return query
        return Coffee.query.filter_by(vendor_id=1)

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
        parser.add_argument('on_sale_date', type=custom_datetime)
        parser.add_argument('imported', type=bool)
        parser.add_argument('imported2', type=bool)
        args = parser.parse_args()
        coffee = Coffee(name=args.name, on_sale_date=args.on_sale_date, vendor_id=1, imported=args.imported)
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
