# tests/test_app.py
import pytest
from flask import url_for
from my_app.app import create_app
from my_app.message import Message

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

def test_message(client):
    res = client.get(url_for('getMessage'))
    assert res.status_code == 200
    assert res.data == b'The App says Hi!'
