import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c

def test_home(client):
    assert client.get('/').status_code == 200

def test_health(client):
    assert client.get('/health').status_code == 200
