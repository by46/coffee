from flask_login import UserMixin

from app import bcrypt
from app import db
from .mixins import UserTypeMixin

UserRole = db.Table('users_roles',
                    db.Column('id', db.Integer, primary_key=True),
                    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                    db.Column('role_id', db.Integer, db.ForeignKey('role.id')))


class User(db.Model, UserMixin, UserTypeMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password_hash = db.Column(db.String(128))
    roles = db.relationship('Role',
                            secondary=UserRole,
                            backref=db.backref('roles', lazy='dynamic'))

    @property
    def password(self):
        raise AttributeError("Password is not readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def verify_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def get_id(self):
        return "builtin_{id}".format(id=self.id)
