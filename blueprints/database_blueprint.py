from flask import Blueprint
from util.json_response import make_json_response
from util.database import reset_database

bp_database = Blueprint(name="bp_database", import_name=__name__, url_prefix="/database")


@bp_database.route("/reset", methods=["POST"])
def database_reset():
    reset_database()
    return make_json_response({"status": "success", "body": "DB Reset"}, 200)
