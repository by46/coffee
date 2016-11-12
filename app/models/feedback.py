from datetime import datetime

from app import db


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True, unique=True)
    coffee_id = db.Column(db.Integer, db.ForeignKey('coffee.id'))
    content = db.Column(db.String(100), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.utcnow)
