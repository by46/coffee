from functools import wraps

from flask import abort
from flask_login import current_user


def wx_required(func):
    return common_required(lambda user: user.is_wx_user)(func)


def manager_required(func):
    return common_required(lambda user: user.is_manager_user)(func)


def common_required(validate_permission):
    """
    common required decorator, used to simple permission validate
    :param validate_permission: `class`:`func`
    :return:
    """

    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if not validate_permission(current_user):
                abort(401)
            return func(*args, **kwargs)

        return decorated_function

    return decorator
