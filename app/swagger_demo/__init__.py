from flask import Blueprint
from flask_restful import Api
from flask_restful import Resource
from flask_restful import fields

main = Blueprint("swagger-demo", __name__, url_prefix="/coffee/swagger-demo")


def swagger_decorate(func):
    print ("Pet swagger_decorate code")
    return func


api = Api(main, decorators=[swagger_decorate])


def add_model(func):
    print(func.__name__)
    return func


class PetResponse(object):
    Name = fields.String

    @classmethod
    def single(cls, func):
        print ("Pet response code")
        func.__resource__ = {'hello': 'benjamin'}
        return func

    @classmethod
    def post(cls, func):
        print ("Pet response post")
        return func


class PetEntity(object):
    @classmethod
    def entity(cls, func):
        def wrapper(*args, **kwargs):
            kwargs['entity'] = {'Title': 'ok'}
            return func(*args, **kwargs)

        return wrapper


@api.resource("/pets")
class Pets(Resource):
    @PetEntity.entity
    @PetResponse.single
    def get(self, entity):
        print(entity)
        return [{'Name': 'coco'}]

    @PetResponse.post
    def post(self):
        return [{'Name': 'coco'}]
