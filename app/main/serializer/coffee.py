from flask_restful import fields

CoffeeResource = {
    'id': fields.Integer,
    'vendor_id': fields.Integer,
    'name': fields.String
}
