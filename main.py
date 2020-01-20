from application_configuration.app import app, db
from models.user import User

def register_blueprints():
    from blueprints.user_blueprint import bp_user
    app.register_blueprint(bp_user)


if __name__ == "__main__":
    register_blueprints()
    db.drop_all()
    db.create_all()
    app.run(debug=True, port=8888)