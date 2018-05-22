from bunch import Bunch

from flask_restful import Api
from flask_restful import Resource

from flask import Flask


class Info(Bunch):
    def __init__(self):
        self.description = None
        self.version = None
        self.title = None
        self.termsOfService = None


class Swagger(Api):
    def __init__(self, version='2.0', **kwargs):
        super(Swagger, self).__init__(**kwargs)
        self.version = version
        self.info = None

    def add_resource(self, resource, *urls, **kwargs):
        print('add_resource')
        super(Swagger, self).add_resource(resource, *urls, **kwargs)

    def json(self):
        pass

    def yaml(self):
        pass


app = Flask(__name__)

api = Swagger(app)


class VersionResponse(object):
    pass


class VersionEntity(object):
    pass


@api.resource("/version")
class Version(Resource):
    @VersionEntity
    @VersionResponse
    def get(self):
        return {'version': '1.0.0'}


if __name__ == '__main__':
    app.run()
