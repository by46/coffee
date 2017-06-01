import posixpath

APP_NAME = '/coffee/'


def make_url_prefix(url_prefix):
    if url_prefix == '/':
        return APP_NAME

    url_prefix = url_prefix.lstrip('/')
    return posixpath.join(APP_NAME, url_prefix)
