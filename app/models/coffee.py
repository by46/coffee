from datetime import datetime

from app import db


class Coffee(db.Model):
    __tablename__ = "coffee"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))
    name = db.Column(db.String(50))
    on_sale_date = db.Column(db.DateTime, default=datetime.utcnow)
