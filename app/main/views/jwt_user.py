from flask_restful import Resource
from flask_restful import fields
from flask_restful import reqparse
from flask_restful_swagger import swagger

from app import jwt
from app.main import api


@jwt.authentication_handler
def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user


@jwt.identity_handler
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)


@swagger.model
class JWTUserModel(object):
    """

    """
    resource_fields = {
        'username': fields.String,
        'password': fields.String,
        'captcha': fields.String
    }


class JWTUserLoginApi(Resource):
    @swagger.operation(notes="JWT login",
                       parameters=[{
                           'name': 'user',
                           'required': True,
                           'dataType': JWTUserModel.__name__,
                           'paramType': 'body'
                       }])
    @jwt.auth_request_handler
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        parser.add_argument('captcha', type=str, required=True)

        args = parser.parse_args()


api.add_resource(JWTUserLoginApi, '/jwt/user/login')
