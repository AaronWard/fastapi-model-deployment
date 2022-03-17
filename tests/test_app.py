"""
This file is to test the robustness of the API

"""

from turtle import reset
import pytest
from fastapi.testclient import TestClient

from main import app

@pytest.fixture(scope="session")
def client():
    client = TestClient(app)
    return client

def test_get(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"msg": "Welcome"}