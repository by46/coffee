
from flask_login import UserMixin


from app import db
from .mixins import UserTypeMixin


class WxUser(db.Model, UserMixin, UserTypeMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    openid = db.Column(db.String(32), unique=True, nullable=False)
    wx_name = db.Column(db.String(32), nullable=False)

    def get_id(self):
        return "wx_{id}".format(id=self.id)

    @property
    def is_wx_user(self):
        return True

    @property
    def is_manager_user(self):
        return False
