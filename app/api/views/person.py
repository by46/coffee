from json import loads

from flask_restful import Resource

from app.api import restful_api


class PersonApi(Resource):
    def get(self):
        with open('app/static/openapi.json', 'r') as reader:
            context = reader.read()
            return loads(context)


restful_api.add_resource(PersonApi, '/persons')
