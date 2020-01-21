import bcrypt


def hash_password(password):
    return bcrypt.hashpw(password, bcrypt.gensalt())


def check_password(password, hash):
    return bcrypt.checkpw(password, hash)