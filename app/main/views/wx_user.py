from flask import abort
from flask_login import current_user
from flask_login import login_user
from flask_restful import Resource
from flask_restful import reqparse
from flask_restful_swagger import swagger

from app.main import api
from app.main.meta import UserModel
from app.models import WxUser


class WxUserApi(Resource):
    @swagger.operation(notes="wx user login",
                       parameters=[{
                           "name": "user",
                           "required": True,
                           "dataType": UserModel.__name__,
                           "paramType": "body"
                       }])
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help="user name")
        parser.add_argument('password', type=str, help="password")
        args = parser.parse_args()
        user = WxUser.query.filter_by(wx_name=args.username).first()
        if user is None:
            abort(401)
        login_user(user)
        return True


api.add_resource(WxUserApi, '/wx_user/login')
