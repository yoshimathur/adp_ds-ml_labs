# tests/test_my_app.py
import pytest
from flask import url_for
from my_greeting_app.app import create_app
from my_greeting_app.greeter import Greeter

# Rest of your test code
@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SERVER_NAME'] = 'localhost:5000'
    return app

@pytest.fixture
def client(app):
    with app.app_context():
        with app.test_client() as client:
            yield client

def test_hello(client):
    res = client.get(url_for('hello'))
    assert res.status_code == 200
    assert res.data == b'Hello, Planet Earth!'
