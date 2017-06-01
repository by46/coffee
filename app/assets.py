from flask_assets import Bundle
from six import iteritems
from webassets.loaders import PythonLoader as PythonAssetsLoader

common_css = Bundle('css/pygments.css', filters='cssmin', output='public/css/common.css')
common_js = Bundle('js/admin.js', 'js/common.js', filters='rjsmin', output='public/css/common.js')


def register_bundle(assets_env):
    loader = PythonAssetsLoader(__name__)
    for name, bundle in iteritems(loader.load_bundles()):
        assets_env.register(name, bundle)
