from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    import gevent.monkey

    gevent.monkey.patch_all()

    from gevent import pywsgi

    server = pywsgi.WSGIServer(("0.0.0.0", 8080), app)
    server.serve_forever()
