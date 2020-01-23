from flask import Blueprint, request
from util.json_response import make_json_response
from util.validators import json_required
from util.database import commit_to_db
from util.password import check_password
from models.user import User

bp_user = Blueprint(name="bp_user", import_name=__name__, url_prefix="/user")


@bp_user.route("/register", methods=["POST"])
@json_required(required_json_headers=["email", "password"])
def register_user():
    user_exist = User.query.filter_by(email=request.json["email"]).first()
    if user_exist is not None:
        return make_json_response({
            "status": "error",
            "body": f"user with email ({request.json['email']}) already exists"}, 400)
    user = User(request.json["email"], request.json["password"])
    commit_to_db(user)
    return make_json_response({"status": "success", "body": "user registered"}, 201)


@bp_user.route("/login", methods=["POST"])
@json_required(required_json_headers=["email", "password"])
def login_user():
    user = User.query.filter_by(email=request.json["email"]).first()

    if user is None:
        return make_json_response({
            "status": "error",
            "message": "Incorrect user information"
        }, 400)

    if not check_password(request.json["password"], user.password):
        return make_json_response({
            "status": "error",
            "message": "Incorrect user information"
        }, 400)

    return make_json_response(user.to_dict(), 200)
