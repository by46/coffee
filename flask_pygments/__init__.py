from flask import url_for

from .extension import PygmentsExtension


def greeting(name=None):
    if name is None:
        name = 'Guy'
    return 'hello, {name}'.format(name=name)


def url_for_with_cached(endpoint, **values):
    return url_for(endpoint, **values)


class Pygments(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.jinja_env.add_extension(PygmentsExtension)
        app.jinja_env.globals.update(greeting=greeting,
                                     url_for_with_cached=url_for_with_cached)
