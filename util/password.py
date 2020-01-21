import bcrypt


def hash_password(password):
    return bcrypt.hashpw(bytes(password, "utf-8"), bcrypt.gensalt())


def check_password(password, hash):
    return bcrypt.checkpw(bytes(password, "utf-8"), hash)