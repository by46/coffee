from flask import Blueprint, Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine.result import ResultProxy

api_blueprint = Blueprint("api", __name__)
api = Api(api_blueprint)
db = SQLAlchemy()


@api.resource("/book/<book_id>")
class Book(Resource):
    def get(self, book_id):
        cmd = """
        SELECT ID, Title
        FROM books WHERE ID=:ID
        """
        cursor = db.session.execute(cmd, params={'ID': book_id})  # type: ResultProxy
        return cursor.fetchone()


settings = {
    'SQLALCHEMY_DATABASE_URI': "mysql+pymysql://root:root@10.16.76.245:3306/coffee"
}


def create(env):
    app = Flask(__name__)
    app.config.from_object(settings)
    db.init_app(app)
    app.register_blueprint(api_blueprint)
    return app


if __name__ == '__main__':
    app = create("prd")
    app.run("0.0.0.0", 8080)
