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

# testing user

def test_read_users():
    response = client.get("/api/user/get")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_user():
    user = {"username": "testuser", "password": "testpass"}
    response = client.post("/api/user/post", json=user)
    assert response.status_code == 201
    assert response.json()["message"] == "Se ha creado el usuario correctamente"

def test_delete_user():
    response = client.get("/api/user/get")
    user_id = response.json()[0]['id']
    response = client.delete(f"/api/user/delete/{user_id}")
    assert response.status_code == 202
    assert response.json()["message"] == "User deleted"

def test_get_user_by_username():
    response = client.get("/api/user/get/testuser2")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser2"

def test_update_user():
    user = {"username": "testuser2", "password": "testpass2"}
    response = client.put("/api/user/put/1", json=user)
    assert response.status_code == 200
    assert response.json()["message"] == f"Se ha modificado el user con id: {response.json()['id']}"