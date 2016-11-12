from flask_login import login_required
from flask_restful import Resource

from app.decorators import wx_required


class BusinessResource(Resource):
    method_decorators = [login_required, wx_required]
