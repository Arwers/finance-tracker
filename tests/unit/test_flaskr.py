from flask import Flask

def test_factory(app):
    """Test that the factory creates a Flask instance."""
    assert isinstance(app, Flask)

def test_database(app):
    """Test that the database was initialized."""
    from flaskr.models import db
    assert db is not None

def test_setup(app):
    """Test that the app has been configured."""
    assert app.limit == 2000
    assert app.categories == [
        "food",
        "car",
        "house",
        "health",
        "taxes",
        "other",
    ]
    assert app.currency == "PLN"

def test_blueprints(app):
    """Test that the blueprints were registered."""
    assert "home" in app.blueprints
    assert "settings" in app.blueprints
    assert "insights" in app.blueprints