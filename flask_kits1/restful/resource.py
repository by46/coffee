from flask_login import login_required
from flask_restful import Resource

from flask_kits1.decorators import wx_required
from flask_kits1.decorators import manager_required


class WxBusinessResource(Resource):
    method_decorators = [login_required, wx_required]


class BusinessResource(Resource):
    method_decorators = [login_required, manager_required]
