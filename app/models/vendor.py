from app import db


class Vendor(db.Model):
    __tablename__ = 'vendor'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50))
