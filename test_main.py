from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_healthcheck():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == "<h1>All good!</h1>"

def test_get_concerts():
    response = client.get("/concerts")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 19
    assert data[0]["date"] == "2025-01-16"
