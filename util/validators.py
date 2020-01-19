from functools import wraps
from flask import request
from util.json_response import make_json_response
from flask import g


def bad_json():
    return make_json_response({"status": "error", "body": "incorrect request JSON"}, 400)


def json_required(required_json_headers):
    def requirements(f):
        @wraps(f)
        def wrap(*args, **kwargs):
            if request.json is None:
                return bad_json()
            for header in required_json_headers:
                if header not in request.json.keys():
                    return bad_json()
            return f(*args, **kwargs)
        return wrap
    return requirements
