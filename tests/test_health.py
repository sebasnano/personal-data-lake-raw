from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_check_returns_api_status() -> None:
    """
    Validate the first public endpoint of the API.

    This test confirms that the service is alive and that the response contract
    stays stable while the project grows.
    """
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "ok"
    assert data["service"] == "personal-data-lake-api"
    assert data["environment"] == "development"
    assert data["version"] == "0.1.0"
