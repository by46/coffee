from flask_restful import fields

FeedbackResource = {
    'id': fields.Integer,
    'coffee_id': fields.Integer,
    'content': fields.String,
    'create_time': fields.DateTime
}
