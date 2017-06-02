from functools import partial

from flask import request
from flask_login import current_user
from flask_menu import MenuEntryMixin
from flask_menu import current_menu


def visible_when(menu_item):
    """

    :param MenuEntryMixin menu_item: 
    :return: 
    """
    role_name = getattr(menu_item, 'role', None)
    if not role_name:
        return True

    for role in current_user.roles:
        if role.name == role_name:
            return True
    return False


def active_when(menu_item):
    """
    
    :param MenuEntryMixin menu_item: 
    :return: 
    """
    if request.endpoint == menu_item._endpoint:
        return True

    return False


def config_menu(app, items):
    """
    items contains menu item, like below
    {'name': 'profile', 'text': 'Home', 'role': 'admin', 'order': 1}
    
    :param flask.Flask app:
    :param list[dict] items:
    
    """
    if not items:
        return

    @app.before_first_request
    def before_first_request():
        for item in items:
            kwargs = item.copy()
            name = kwargs.pop('name')
            menu_item = current_menu.submenu(name)  # type: MenuEntryMixin
            kwargs['endpoint'] = None
            kwargs['visible_when'] = partial(visible_when, menu_item)
            kwargs['active_when'] = active_when
            menu_item.register(**kwargs)
