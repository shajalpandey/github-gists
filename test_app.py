import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_gists_success(client):
    response = client.get('/octocat')  # Replace 'octocat' with a valid GitHub username
    assert response.status_code == 200
    assert isinstance(response.json, list)
    print(response.json)

def test_invalid_user(client):
    response = client.get('/nonexistentuserbbb')
    assert response.status_code == 404
    print(response.json)
