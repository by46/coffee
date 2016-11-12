from flask_restful import fields

from .feedback import FeedbackResource

CoffeeResource = {
    'id': fields.Integer,
    'vendor_id': fields.Integer,
    'name': fields.String,
    'on_sale_date': fields.DateTime,
    'imported': fields.Boolean,
    'feedbacks': fields.List(fields.Nested(FeedbackResource))
}
