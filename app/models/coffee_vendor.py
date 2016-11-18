from app import db

CoffeeVendor = db.table('coffee_vendor',
                        db.Column('coffee_id', db.Integer, db.ForeignKey('coffee.id')),
                        db.Column('vendor_id', db.Integer, db.ForeignKey('vendor.id')))
