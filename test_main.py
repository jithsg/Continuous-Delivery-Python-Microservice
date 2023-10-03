from fastapi.testclient import TestClient
from main import app  # Adjust the import to your file structure

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Wikipedia API": "Welcome to the Wikipedia API"}


def test_wiki():
    response = client.get("/wiki/War Goddess")
    assert response.status_code == 200
    # Assuming the summary for "War Goddess" contains the word "Goddess"
    assert "god" in response.json().get("result", "")


def test_search():
    response = client.get("/search/War Goddess")
    assert response.status_code == 200
    # Assuming the search for "War Goddess" returns a non-empty list
    assert len(response.json().get("result", [])) > 0
