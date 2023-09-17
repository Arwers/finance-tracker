from flask import Flask


def create_app(config_filename="config.py"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config")
    app.config.from_pyfile(config_filename)

    # database
    from .models import db
    db.init_app(app)
    app.app_context().push()

    # blueprints
    from .homepage.views import homepage
    app.register_blueprint(homepage)
    
    return app
