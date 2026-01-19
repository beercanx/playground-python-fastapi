from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.hello import hello

fastAPI = FastAPI()
fastAPI.include_router(hello.router)

client = TestClient(fastAPI)


def test_say_hello():
    response = client.get("/hello/aardvark")

    assert response.status_code == 200

    data = response.json()
    assert data["message"] == "Hello aardvark"


def test_say_hello_missing_name():
    response = client.get("/hello")

    assert response.status_code == 404

    data = response.json()
    assert data["detail"] == "Not Found"
