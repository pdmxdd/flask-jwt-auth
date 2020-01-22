from application_configuration.app import db


def reset_database():
    from models.user import User
    db.drop_all()
    db.create_all()


def commit_to_db(some_model):
    db.session.add(some_model)
    db.session.commit()