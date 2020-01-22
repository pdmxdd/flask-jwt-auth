from application_configuration.app import db
from util.password import hash_password


class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.LargeBinary)

    def __init__(self, email, password):
        self.email = email
        self.password = hash_password(password)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email
        }
