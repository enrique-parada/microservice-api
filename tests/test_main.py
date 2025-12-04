from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


def test_info():
    resp = client.get("/info")
    assert resp.status_code == 200
    data = resp.json()
    assert data["service"] == "devops-text-toolkit"
    assert "version" in data
    assert "environment" in data


def test_analyze_text_basic():
    payload = {"text": "Hola DevOps 123"}
    resp = client.post("/analyze", json=payload)
    assert resp.status_code == 200
    data = resp.json()

    assert data["text"] == payload["text"]
    assert data["length"] == len(payload["text"])
    assert data["word_count"] == len(payload["text"].split())
    assert data["has_numbers"] is True
    assert data["has_uppercase"] is True


def test_analyze_text_empty():
    payload = {"text": ""}
    resp = client.post("/analyze", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["length"] == 0
    assert data["word_count"] == 0


def test_analyze_password():
    payload = {"password": "Abcdef12"}
    resp = client.post("/analyze/password", json=payload)
    assert resp.status_code == 200
    data = resp.json()

    assert data["length"] == len(payload["password"])
    assert data["has_numbers"] is True
    assert data["has_uppercase"] is True
    assert data["score"] >= 2

