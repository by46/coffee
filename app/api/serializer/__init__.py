from flask_kits.restful import Serializer

from app.models import User


class UserSerializer(Serializer):
    __model__ = User
