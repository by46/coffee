# -:- coding:utf8 -:-
"""

"""
__author__ = 'benjamin.c.yan'
__version__ = '0.0.1'


class Kits(object):
    def __init__(self, app=None, **kwargs):
        self._app = None
        self._options = {}
        if app:
            self.init_app(app, **kwargs)

    def init_app(self, app, **kwargs):
        self._app = app
        self._options.update(kwargs)
