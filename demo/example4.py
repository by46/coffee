from flask import Flask
from flask_compress import Compress
from flask_cors import CORS
from flask_redis import FlaskRedis

settings = {
    'CORS_ORIGINS': "*",
    'CORS_METHODS': 'GET,POST,PUT',
    'CORS_ALLOW_HEADERS': 'Content-Type,Host',
    'COMPRESS_MIN_SIZE': 64 << 10,
    'REDIS_URL': 'redis://localhost:6379/0'
}

cors = CORS()
compress = Compress()
redis = FlaskRedis()


def create(env):
    app = Flask(__name__)
    app.config.from_object(settings)

    cors.init_app(app)
    compress.init_app(app)
    redis.init_app(app)
    return app


if __name__ == '__main__':
    app = create("prd")
    app.run("0.0.0.0", 8080)
