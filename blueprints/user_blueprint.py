from flask import Blueprint

bp_user = Blueprint(name="bp_user", import_name=__name__, url_prefix="/user")


@bp_user.route("/register", methods=["POST"])
def register_user():
    return "success"
