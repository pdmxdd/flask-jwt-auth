import os
from application_configuration.app import app


def register_blueprints():
    from blueprints.user_blueprint import bp_user
    app.register_blueprint(bp_user)

    from blueprints.database_blueprint import bp_database
    app.register_blueprint(bp_database)


if __name__ == "__main__":
    register_blueprints()
    app.run(debug=True, port=os.environ.get("API_PORT"))