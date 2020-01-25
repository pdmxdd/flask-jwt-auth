from functools import wraps
from flask import request, g
from util.json_response import make_json_response
from util.authorization import verify_token


def bad_json():
    return make_json_response({"status": "error", "body": "incorrect request JSON"}, 400)


def missing_json():
    return make_json_response({"status": "error", "body": "JSON missing"}, 400)


def json_required(required_json_headers):
    def requirements(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if request.json is None:
                return missing_json()
            for header in required_json_headers:
                if header not in request.json.keys():
                    return bad_json()
            return f(*args, **kwargs)
        return wrap
    return requirements


def jwt_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "Authorization" not in request.headers.keys():
            return make_json_response({"status": "error", "body": "Missing JWT authorization"}, 401)

        payload = verify_token(request.headers.get("Authorization"), request.remote_addr)

        if not payload["success"]:
            return make_json_response({"status": "error", "body": "Unauthorized"}, 401)

        g.payload = payload["payload"]

        return f(*args, **kwargs)
    return wrap
