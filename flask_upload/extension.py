from flask_upload.views import upload_blueprint

URL_PREFIX = 'x'
missing = object()


class Upload(object):
    def __init__(self, app=None, **kwargs):
        self._options = {}
        self._app = None
        if app is not None:
            self.init_ap(app, **kwargs)

    def init_app(self, app, **kwargs):
        self._app = app
        self._options.update(kwargs)
        upload_blueprint.url_prefix = self.get_parameter('url_prefix')
        app.register_blueprint(upload_blueprint)

    def get_parameter(self, name, default=None):
        option = self._options.get(name, missing)
        if option is missing:
            parameter_name = 'UPLOAD_{0}'.format(name.upper())
            option = self._app.config.get(parameter_name, default)
        return option
