import os
import json
from flask import make_response


def make_json_response(some_dict, http_status):
    response = make_response(json.dumps(some_dict), http_status)
    response.headers.add('Content-Type', 'application/json')

    # Enable CORS for front end
    response.headers.add('Access-Control-Allow-Origin', f'{os.environ.get("FRONT_END")}')
    return response
