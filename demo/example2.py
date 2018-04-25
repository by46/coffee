from random import randint

from flask import Blueprint, Flask
from flask_kits.restful.entity import EntityBase, Field, Response
from flask_restful import Api, Resource, fields
from flask_restful_swagger import swagger

api_blueprint = Blueprint("api", "api", url_prefix="/demo")
api = swagger.docs(Api(api_blueprint), apiVersion="0.0.1")


class BookResponse(Response):
    ID = fields.Integer
    Title = fields.String


class BookEntity(EntityBase):
    Title = Field("Title", type=unicode, required=True)


class Books(Resource):
    @BookEntity.parameter
    @BookResponse.single
    def post(self, entity):
        """create new book"""
        return {"ID": randint(0, 100), "Title": entity.Title}


api.add_resource(Books, "/book/")


class Book(Resource):
    @BookResponse.single
    def get(self, book_id):
        """get one book
        
        this is a awesome book
        """
        return {"ID": book_id, "Title": "Python program"}


api.add_resource(Book, "/book/<book_id>")


def create(env):
    app = Flask(__name__)
    app.register_blueprint(api_blueprint)
    return app


if __name__ == '__main__':
    app = create("prd")
    app.run("0.0.0.0", 8080)
