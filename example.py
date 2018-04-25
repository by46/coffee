from flask import Flask
from flask_restful import Api
from flask_restful import Resource

app = Flask(__name__)

api = Api(app)


@api.resource("/books")
class Books(Resource):
    def get(self):
        return [{"Title": "Python program"}]

    def post(self):
        return [{"Title": "Python program"}]


if __name__ == '__main__':
    app.run("0.0.0.0", 8080)
