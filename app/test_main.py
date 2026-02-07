import os
import pytest
from main import app

@pytest.fixture
def test1(monkeypatch):
    monkeypatch.setenv("WEB_API_PORT", "5000")
    monkeypatch.setenv("WEB_API_VALUE", "test_value")
    
    # Enable Flask testing mode
    app.config["TESTING"] = True
    with app.test_client() as test1:
        yield test1

def test_health(test1):
    """Test /health endpoint"""
    response = test1.get("/health")
    assert response.status_code == 200
    assert response.data == b"OK"
    assert os.getenv("WEB_API_PORT") == "5000"


def test_value(test1):
    """Test /health endpoint"""
    response = test1.get("/value")
    assert response.status_code == 200
    assert os.getenv("WEB_API_VALUE") == "test_value"
    assert os.getenv("WEB_API_PORT") == "5000"
