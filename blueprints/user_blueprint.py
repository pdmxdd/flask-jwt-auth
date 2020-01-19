from flask import Blueprint, request
from util.json_response import make_json_response
from util.validators import json_required

bp_user = Blueprint(name="bp_user", import_name=__name__, url_prefix="/user")


# @json_required(required_json_headers=["email", "password"])
@bp_user.route("/register", methods=["POST"])
@json_required(required_json_headers=["email", "password"])
def register_user():
    return make_json_response({"status": "success", "body": "user registered"}, 201)
