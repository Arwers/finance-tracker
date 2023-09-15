from flask import Flask
from .homepage.views import homepage
from flask_sqlalchemy import SQLAlchemy

# app
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

#blueprints
app.register_blueprint(homepage)

# database
db = SQLAlchemy(app)
from .models import Expenses, Users
