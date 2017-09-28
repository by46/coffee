# -:- coding:utf8 -:-
from flask_restful import Resource
from flask_restful import abort
from flask_restful import fields
from flask_restful.reqparse import RequestParser
from flask_restful_swagger import swagger

from app.api import restful_api
from app.api.serializer import UserSerializer
from app.models import User


def item_builder(item):
    return item


class UsersApi(Resource):
    @UserSerializer.parameter('dfis', data_type='int')
    @UserSerializer.list(item_builder=item_builder)
    def get(self):
        """获取所有用户
        """
        return User.query

    @UserSerializer.parameter('entity', data_type=UserSerializer, param_type='body')
    @UserSerializer.single
    def post(self):
        """新增用户
        """
        entity = User()
        return entity


restful_api.add_resource(UsersApi, '/users')


class UserApi(Resource):
    @UserSerializer.single
    def get(self, user_id):
        """获取单个User信息
        """
        entity = User.query.get_or_404(user_id)
        return entity

        abort(400, error_message="just accept on appoint on special date")

    @UserSerializer.single
    def delete(self, user_id):
        """删除用户
        """
        return User.query.get_or_404(user_id)


restful_api.add_resource(UserApi, '/user/<int:user_id>')


@swagger.model
class Entity(object):
    resource_fields = {
        "types": fields.Integer
    }


class User3Api(Resource):
    @swagger.operation(notes="xxx",
                       parameters=[{
                           'name': 'entity',
                           'dataType': Entity.__name__,
                           'paramType': 'body'
                       }])
    def post(self):
        parser = RequestParser()
        parser.add_argument('types', type=int, choices=(-1, 0, 1))
        args = parser.parse_args()
        print(args)
        return {}


restful_api.add_resource(User3Api, '/user3')
