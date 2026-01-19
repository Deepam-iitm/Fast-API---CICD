from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome !!"}


def test_simple_interest_success():
    payload = {
        "principal": 2000,
        "rate": 5,
        "time": 2
    }

    response = client.post("/si", json=payload)

    assert response.status_code == 200

    data = response.json()
    assert data["principal"] == 2000
    assert data["interest"] == 200.0
    assert data["total_amount"] == 2200.0


def test_simple_interest_validation_error():
    payload = {
        "principal": 500,   # ❌ less than gt=1000
        "rate": 5,
        "time": 2
    }

    response = client.post("/si", json=payload)

    assert response.status_code == 422
