from datetime import datetime

from sqlalchemy import Index

from app import db


class Coffee(db.Model):
    __tablename__ = "coffee"
    __table_args__ = (Index('idx_coffee_name_imported', 'name', 'imported'),)
    id = db.Column(db.Integer, primary_key=True, unique=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))
    name = db.Column(db.String(50))
    imported = db.Column(db.Boolean, default=True)
    on_sale_date = db.Column(db.DateTime, default=datetime.utcnow)
    feedbacks = db.relationship('Feedback',
                                backref='coffee', lazy='dynamic')

    def __repr__(self):
        return "<Coffee {0}>".format(self.id)
