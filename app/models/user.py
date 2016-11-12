from flask_login import UserMixin

from app import db
from .mixins import UserTypeMixin


class User(db.Model, UserMixin, UserTypeMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(32), nullable=False)

    def get_id(self):
        return "builtin_{id}".format(id=self.id)