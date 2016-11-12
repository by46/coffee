from flask_restful import fields
from flask_restful_swagger import swagger


@swagger.model
class UserModel(object):
    """
    Used to login
    """
    resource_fields = {
        "username": fields.String,
        "password": fields.String
    }
