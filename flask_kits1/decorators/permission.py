from functools import wraps

from flask import abort
from flask_login import current_user


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.has_permission(permission):
                abort(401)
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def admin_required(f):
    return permission_required()(f)


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


def wx_required(func):
    """
    require wx login
    :param func:
    :return:
    """
    return common_required(lambda user: user.is_wx_user)(func)


def manager_required(func):
    """
    require portal login
    :param func:
    :return:
    """
    return common_required(lambda user: user.is_manager_user)(func)
