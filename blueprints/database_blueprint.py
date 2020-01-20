from flask import Blueprint
from util.json_response import make_json_response

bp_database = Blueprint(name="bp_database", import_name=__name__, url_prefix="/database")


@bp_database.route("/reset", methods=["POST"])
def database_reset():
    from application_configuration.app import db
    from models.user import User
    db.drop_all()
    db.create_all()
    return make_json_response({"status": "success", "body": "DB Reset"}, 200)
