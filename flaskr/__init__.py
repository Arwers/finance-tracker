from flask import Flask, current_app

def create_app(config_filename="config.py"):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config")
    app.config.from_pyfile(config_filename)

    # database
    from .models import db
    db.init_app(app)
    app.app_context().push()

    # context variables
    current_app.limit = 2000
    current_app.categories = [
        "food",
        "car",
        "house",
        "health",
        "taxes",
        "other",
    ]

    # blueprints
    from .homepage.views import homepage
    from .settings.views import settings
    app.register_blueprint(homepage)
    app.register_blueprint(settings)

    return app
