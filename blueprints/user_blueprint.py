from flask import Blueprint
from util.json_response import make_json_response

bp_user = Blueprint(name="bp_user", import_name=__name__, url_prefix="/user")


@bp_user.route("/register", methods=["POST"])
def register_user():
    return make_json_response({"status": "success", "body": "user registered"}, 201)
