from flask import Flask


# app
def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config")
    app.config.from_pyfile("config.py")

    # database
    from .models import db
    db.init_app()

    # blueprints
    from .homepage.views import homepage
    app.register_blueprint(homepage)
