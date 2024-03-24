from flask import Flask
from flask.testing import FlaskClient
from flaskr.insights.views import insights

def test_index():
    app = Flask(__name__)
    app.register_blueprint(insights)

    with app.test_client() as client:
        response = client.get("/insights")