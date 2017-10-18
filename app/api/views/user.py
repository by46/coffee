# -:- coding:utf8 -:-

from decimal import Decimal

from flask_restful import Resource
from flask_restful import abort
from flask_restful import fields
from flask_restful.reqparse import RequestParser
from flask_restful_swagger import swagger
from sqlalchemy import types
from sqlalchemy.engine.result import ResultProxy
from sqlalchemy.sql import outparam

from app import db
from app.api import restful_api
from app.api.serializer import UserSerializer
from app.models import User
from app.utils.common import select_bind
from .parser import EntityBase
from .parser import Field
from .parser import LetterValidator
from .parser import MaxLengthValidator
from .parser import MinLengthValidator
from .parser import MoreValidator
from .parser import PrecisionValidator
from .parser import parameter


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
        "Types": fields.Integer,
        "Name": fields.String
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


class User4Api(Resource):
    @UserSerializer.single
    def get(self):
        cmd = """
        SELECT id, name, password_hash FROM user
        """
        bind = select_bind('coffee02')
        result = db.session.execute(cmd, bind=bind)  # type: ResultProxy
        return result.fetchall()

    @UserSerializer.single
    def post(self):
        connection = db.session.bind.raw_connection()
        try:
            cursor = connection.cursor()
            cursor.callproc("new_user", (None,))
            cursor.fetchall()
            cursor.execute('SELECT @_new_user_0')
            result = cursor.fetchone()
            print(result)
            cursor.close()
            connection.commit()
        finally:
            connection.close()
        bind = select_bind('coffee02')
        msg = outparam('msg', type_=types.String)
        params = [msg]
        # sp_call = text('CALL new_user)', bindparams=params)
        result = db.session.execute('CALL new_user(:msg)', params={'msg': 1})  # type: ResultProxy
        return result.fetchall()

    @UserSerializer.single
    def put(self):
        bind1 = select_bind('coffee01')
        bind2 = select_bind('coffee02')
        cmd = "INSERT INTO demo5(name) VALUES(:Name);"

        result = db.session.execute(cmd, params={'Name': 1}, bind=bind1)  # type: ResultProxy
        print(result.returns_rows)
        result2 = db.session.execute(cmd, params={'Name': 'benjamin2'}, bind=bind2)
        print(result.returns_rows)
        db.session.commit()

    @UserSerializer.single
    def delete(self):
        db.session.execute("INSERT INTO demo5(name) VALUES (:Name)", params={'Name': 'benjamin1'})
        db.session.execute("INSERT INTO demo5(name) VALUES (:Name)", params={'Name': 'benjamin2'})
        db.session.begin_nested()
        db.session.execute("INSERT INTO demo5(name) VALUES (:Name)", params={'Name': 'benjamin3'})
        db.session.rollback()
        db.session.begin_nested()
        db.session.execute("INSERT INTO demo5(name) VALUES (:Name)", params={'Name': 'benjamin4'})
        db.session.commit()
        db.session.commit()


restful_api.add_resource(User4Api, '/user4')


class AddressEntity(EntityBase):
    Zip = Field("Zip")


class UserEntity(EntityBase):
    # Name = Field('Name', location='json', type=str, validators=[MinLengthValidator(5), MaxLengthValidator(10)])
    # Age = Field('Age', type=int, validators=[MoreValidator(10), LetterValidator(15)])
    # Sex = Field('Sex', type=bool, default=True)
    # Amount = Field('Amount', type=Decimal,
    #                validators=[MoreValidator(Decimal('10.1')),
    #                            LetterValidator(Decimal("12.9")),
    #                            PrecisionValidator(2)])
    Address = Field('Address', type=AddressEntity)

    def validate(self):
        if self.Sex:
            return True
        return ValueError("Must be female")


class User5Api(Resource):
    @UserSerializer.parameter(data_type=Entity)
    @UserSerializer.single
    def post(self, user_id):
        parser = RequestParser()
        parser.add_argument('Name', action='append')
        parser.add_argument('Address')
        args = parser.parse_args()
        print(args)
        entity = UserEntity.parse()
        print(entity.Name)
        print(isinstance(entity, dict))
        entity.ApplicationID = 123456
        print(entity, entity.ApplicationID)

    @parameter(UserEntity)
    @UserSerializer.single
    def put(self, user_id, entity):
        print(user_id, entity.Name)


restful_api.add_resource(User5Api, '/user5/<int:user_id>')
