import os
import datetime
import binascii
import jwt


def get_jwt_secret():
    # This method either gets or creates a new jwt secret
    if "jwt_secret" not in os.environ.keys():
        if os.path.isfile('jwt_secret.txt'):
            with open('jwt_secret.txt', 'r') as f:
                os.environ["jwt_secret"] = f.read()
        else:
            jwt_secret = binascii.hexlify(os.urandom(32)).decode()
            # jwt_secret = Fernet.generate_key().decode()
            with open('jwt_secret.txt', 'w') as f:
                f.write(jwt_secret)
            os.environ["jwt_secret"] = jwt_secret
    return os.environ["jwt_secret"]


def assign_token(payload, ip_address, lifetime_hours=6):
    payload["ip_address"] = ip_address
    payload["iat"] = datetime.datetime.utcnow()
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(seconds=(lifetime_hours*60*60))
    encoded_token = jwt.encode(
        payload,
        get_jwt_secret(),
        algorithm='HS256'
    )
    return encoded_token.decode('utf-8')


def verify_token(token_string, ip_address):
    key = get_jwt_secret()
    if token_string == "":
        return {"success": False, "status": "JWT error. No JWT provided"}
    try:
        decoded_token = jwt.decode(str.encode(token_string), key, algorithms=['HS256'])
        if decoded_token["ip_address"] != ip_address:
            # TODO: log this as a possible attack
            return {"success": False, "status": "JWT error. IP Addresses don't match! User needs to re-authenticate."}
    except jwt.ExpiredSignatureError:
        # need to return JSON error that token is expired
        # return False
        return {"success": False, "status": "JWT expired. User must re-authenticate for a new token."}
    except jwt.exceptions.InvalidSignatureError:
        return {"success": False, "status": "JWT error. User needs to re-authenticate."}
    except jwt.exceptions.DecodeError:
        return {"success": False, "status": "JWT error. User needs to re-authenticate."}
    return {"success": True, "payload": jwt.decode(str.encode(token_string), key, algorithms=['HS256'])}
