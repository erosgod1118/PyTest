import requests 
import app 
import pytest

class MockResponse:
    @staticmethod 
    def json():
        return {"mock_key": "mock_response"}
    
@pytest.fixture
def mock_response(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()
    
    monkeypatch.setattr(requests, "get", mock_get)

def test_get_json(mock_response):
    result = app.get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"

@pytest.fixture 
def mock_test_user(monkeypatch):
    monkeypatch.setitem(app.DEFAULT_CONFIGS, "user", "test_user")

@pytest.fixture 
def mock_test_database(monkeypatch):
    monkeypatch.setitem(app.DEFAULT_CONFIGS, "database", "test_db")

@pytest.fixture 
def mock_missing_default_user(monkeypatch):
    monkeypatch.delitem(app.DEFAULT_CONFIGS, "user", raising=False)

def test_connection(mock_test_user, mock_test_database):
    expected = "User Id=test_user; Location=test_db;"

    result = app.create_connection_string()
    assert result == expected

def test_missing_user(mock_missing_default_user):
    with pytest.raises(KeyError):
        _ = app.create_connection_string()