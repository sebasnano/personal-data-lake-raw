from fastapi.testclient import TestClient

from app.main import app


class FakeMinioClient:
    """
    Fake MinIO client used by the API route test.

    It simulates that the RAW bucket already exists.
    """

    def bucket_exists(self, bucket_name: str) -> bool:
        return True

    def make_bucket(self, bucket_name: str) -> None:
        raise AssertionError("make_bucket should not be called")


client = TestClient(app)


def test_storage_health_endpoint_returns_storage_status(monkeypatch) -> None:
    """
    The storage health endpoint should return the object storage status.

    The MinIO client is replaced with a fake client so this test can run without
    Docker or a real MinIO service.
    """

    def fake_get_minio_client() -> FakeMinioClient:
        return FakeMinioClient()

    monkeypatch.setattr(
        "app.routes.storage_health.get_minio_client",
        fake_get_minio_client,
    )

    response = client.get("/health/storage")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"
    assert data["bucket"] == "raw"
    assert data["available"] is True
    assert data["message"] == "RAW bucket already exists."
