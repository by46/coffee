from app import db

coffee_vendor = db.Table('coffee_vendor',
                         db.Column('id', db.Integer, primary_key=True),
                         db.Column('coffee_id', db.Integer, db.ForeignKey('coffee.id')),
                         db.Column('vendor_id', db.Integer, db.ForeignKey('vendor.id')))

demo2 = db.Table('demo2', db.Column('id', db.Integer, primary_key=True), mysql_engine='InnoDB')
