from fastapi.testclient import TestClient

from src.ml_inference_server.main import app

client = TestClient(app)


def test_get_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_post_analyze_valid():
    response = client.post("/analyze", json={"image_url": "https://temp.com"})
    assert response.status_code == 200
    created_job_id = response.json()["job_id"]
    assert created_job_id == client.get(f"/jobs/{created_job_id}").json()["job_id"]


def test_post_analyze_empty():
    response = client.post("/analyze", json={"image_url": ""})
    assert response.status_code == 422


def test_post_analyze_missing_body():
    response = client.post("/analyze", json={})
    assert response.status_code == 422


def test_get_jobs_unknown():
    response = client.get("/jobs/unknown_id")
    assert response.status_code == 404
