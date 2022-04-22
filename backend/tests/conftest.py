from app import flask_app
import pytest

@pytest.fixture
def app():
    app=flask_app()
    app.config.update({"TESTING":True,})
    yield app

@pytest.fixture
def test_client(app):
    client=app.test_client()
    return client

