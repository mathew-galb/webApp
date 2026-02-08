import os
import pytest
from main import app

"""
Used these documentation as a starter.
https://code.visualstudio.com/docs/python/testing
https://docs.pytest.org/en/stable/getting-started.html

Found that monkeypatch was a way to simulate environement variables
https://docs.pytest.org/en/stable/how-to/monkeypatch.html

took a while to find a way to get env through monkey patch but found that documentation
makes use of os lib again.

"""

@pytest.fixture
def test1(monkeypatch):
    monkeypatch.setenv("WEB_API_PORT", "3000")
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
    assert os.getenv("WEB_API_PORT") == "3000"
    

"""
This test help me find out the way I was returning value was wrong
"""
def test_value(test1):
    """Test /health endpoint"""
    response = test1.get("/value")
    assert response.status_code == 200
    assert response.data == b"test_value"
    assert os.getenv("WEB_API_VALUE") == "test_value"
    assert os.getenv("WEB_API_PORT") == "3000"
    

#################################################

