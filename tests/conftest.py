from flaskr import create_app
import pytest

@pytest.fixture()
def app():
    app = create_app("testconfig.py")
    yield app

@pytest.fixture()
def client(app):
    return app.test_client()