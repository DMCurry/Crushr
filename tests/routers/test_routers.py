import pytest
import pdb
import deepdiff
from fastapi.testclient import TestClient
from router_test_data import test_get_exercises_data

def test_get_exercises(client: TestClient):
    response = client.get("/exercises")
    assert response.status_code == 200
    assert deepdiff.DeepDiff(response.json(), test_get_exercises_data, ignore_order=True) == {}

