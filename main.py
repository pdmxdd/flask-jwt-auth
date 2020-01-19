from application_configuration.app import app


def register_blueprints():
    from blueprints.user_blueprint import bp_user
    app.register_blueprint(bp_user)


if __name__ == "__main__":
    register_blueprints()
    app.run(debug=True, port=8888)