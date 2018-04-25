from app.portal import portal
from flask import request


@portal.route("/pypi", methods=['POST'])
def repository():
    content = request.files["content"]
    content.save("content.tar.gz")
    return "success"
