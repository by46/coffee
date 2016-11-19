from flask_jwt import jwt_required
from flask_restful import Resource
from flask_restful_swagger import swagger

from app.main import api


class EverNone(Resource):
    @swagger.operation(notes="Get special note",
                       parameters=[{
                           'name': 'note_id',
                           'required': True,
                           'dataType': 'int',
                           'paramType': 'path'
                       }, {
                           'name': 'authorization',
                           'required': True,
                           'dataType': 'str',
                           'paramType': 'header'
                       }])
    @jwt_required()
    def get(self, note_id):
        return {'id': note_id}


api.add_resource(EverNone, '/evernote/<int:note_id>')
