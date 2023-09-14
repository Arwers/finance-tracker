from flask import Flask
from .homepage.views import homepage
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

#blueprints
app.register_blueprint(homepage)