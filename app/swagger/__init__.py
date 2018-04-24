from flask import Blueprint
from flask import render_template

swagger = Blueprint("swagger", __name__, url_prefix="/coffee/swagger")


@swagger.route("/spec.html", methods=["GET"])
def spec():
    return render_template("swagger/index.html")


@swagger.route("/spec.json", methods=["GET"])
def json():
    return render_template("swagger/pet.json")
