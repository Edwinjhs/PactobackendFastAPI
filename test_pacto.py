from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_token():
    response = client.post("/token/", data={"username": "testuser", "password": "testpass"})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_invalid_token():
    response = client.post("/token/", data={"username": "invaliduser", "password": "invalidpass"})
    assert response.status_code == 401
    assert "detail" in response.json()
    assert response.json()["detail"] == "Incorrect username or password"
