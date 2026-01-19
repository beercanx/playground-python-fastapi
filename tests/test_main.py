from fastapi.testclient import TestClient

from app.main import application

client = TestClient(application)


def test_root():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()
    assert data["message"] == "Hello, World!"
