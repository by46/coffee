from flask_restful import fields
from flask_restful_swagger import swagger


@swagger.model
class CoffeeModel(object):
    resource_fields = {
        "name": fields.String,
        "on_sale_date": fields.DateTime,
        "imported": fields.Boolean,
        "imported2": fields.Boolean
    }
