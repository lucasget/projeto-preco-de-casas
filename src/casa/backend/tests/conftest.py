import pytest
from fastapi.testclient import TestClient
from casa.backend.fastapi_zero.app import app


@pytest.fixture
def client():
    return TestClient(app)  # arrange
