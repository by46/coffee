class UserTypeMixin(object):
    @property
    def is_wx_user(self):
        return False

    @property
    def is_manager_user(self):
        return True
