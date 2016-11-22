import httplib

import requests
from qiniu import Auth
from qiniu import put_data

from flask_upload.views import upload_blueprint

URL_PREFIX = 'url_prefix'
ACCESS_KEY = 'qiniu_access_key'
SECRET_KEY = 'qiniu_secret_key'
BUCKET = 'qiniu_bucket'
HOST = 'qiniu_cdn'

missing = object()


class Upload(object):
    def __init__(self, app=None, **kwargs):
        self._options = {}
        self._app = None
        self._access_key = None
        self._secret_key = None
        self._bucket = None
        self._host = None
        if app is not None:
            self.init_ap(app, **kwargs)

    def init_app(self, app, **kwargs):
        self._app = app
        self._options.update(kwargs)
        self._access_key = self.get_parameter(ACCESS_KEY, app=app)
        self._secret_key = self.get_parameter(SECRET_KEY, app=app)
        self._bucket = self.get_parameter(BUCKET, app=app)
        self._host = self.get_parameter(HOST, app=app)

        self._app.upload = self
        upload_blueprint.url_prefix = self.get_parameter(URL_PREFIX, app=app)
        app.register_blueprint(upload_blueprint)

    def get_parameter(self, name, default=None, app=None):
        option = self._options.get(name, missing)
        if option is missing:
            parameter_name = 'UPLOAD_{0}'.format(name.upper())
            option = app.config.get(parameter_name, default)
        return option

    def get_auth(self):
        pass

    def __make_url(self, key):
        return "{0}/{1}".format(self._host, key)

    def upload(self, key, content, mime_type):
        url = self.__make_url(key)
        response = requests.head(url)
        if response.status_code == httplib.OK:
            return response.headers.get('etag').strip("\"")
        q = Auth(self._access_key, self._secret_key)
        token = q.upload_token(self._bucket, key, 3600)
        ret, response = put_data(token, key, content, mime_type=mime_type)
        if response.status_code == httplib.OK:
            return url, ret.get('hash')
        return None, None
