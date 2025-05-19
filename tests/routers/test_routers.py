import pytest
from fastapi.testclient import TestClient

def test_get_exercises(client: TestClient):
    response = client.get("/exercises")
    assert response.status_code == 200
    print(response.json)
