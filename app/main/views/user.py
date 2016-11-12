from flask import abort
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_restful import Resource
from flask_restful import reqparse
from flask_restful_swagger import swagger

from app.main import api
from app.main.meta import UserModel
from app.models import User


class LoginApi(Resource):
    @swagger.operation(notes="get current user")
    def get(self):
        if hasattr(current_user, 'name'):
            return getattr(current_user, 'name')
        return getattr(current_user, 'wx_name')

    @swagger.operation(notes="user login",
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

        user = User.query.filter_by(name=args.username).first()
        if user is None:
            abort(401)

        login_user(user)
        return True


api.add_resource(LoginApi, '/user/login')


class LogoutApi(Resource):
    @swagger.operation(notes="login current user")
    def post(self):
        logout_user()


api.add_resource(LogoutApi, '/user/logout')
