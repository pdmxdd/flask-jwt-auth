from flask import Blueprint, request, g
from util.json_response import make_json_response
from util.validators import json_required, jwt_required
from util.database import commit_to_db
from util.password import check_password
from models.user import User
from util.authorization import assign_token

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
    return make_json_response({
        "status": "success",
        "body": "user registered",
        "token": assign_token(user.to_dict(), request.remote_addr)}
        , 201)


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

    return make_json_response({"status": "success",
                               "message": "user authenticated",
                               "token": assign_token(user.to_dict(), request.remote_addr)}
                              , 200)


@bp_user.route("/account", methods=["GET"])
@jwt_required
def get_user_account():
    payload = g.payload
    return make_json_response(payload, 200)


@bp_user.route("/account", methods=["POST"])
@jwt_required
@json_required(["email", "new_password", "confirm_password"])
def post_user_account():
    payload = g.payload
    print(payload)
    user = User.query.filter_by(id=payload.get('id')).first()
    if user is None:
        return make_json_response({"status": "error", "message": "JWT error. User must re-authenticate."}, 400)
    if request.json.get('new_password') != request.json.get('confirm_password'):
        return make_json_response({"status": "error", "message": "Passwords don't match!"}, 400)
    user.update_password(request.json.get('new_password'))
    commit_to_db(user)
    return make_json_response({"status": "success", "message": "Account successfully updated"}, 200)
