from application_configuration.app import db


def commit_to_db(some_model):
    db.session.add(some_model)
    db.session.commit()