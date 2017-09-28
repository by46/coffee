from app import login_manager
from app.models import User
from app.models import WxUser
from . import coffee
from . import evernote
from . import index
from . import misc
from . import user
from . import vue
from . import wx_user

PREFIX_WX = "wx_"
PREFIX_BUILTIN = 'builtin_'


@login_manager.user_loader
def load_user(user_id):
    if user_id.startswith(PREFIX_WX):
        return WxUser.query.get(user_id[len(PREFIX_WX):])
    else:
        return User.query.get(user_id[len(PREFIX_BUILTIN):])
