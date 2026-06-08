from app.storage.storage_service import ObjectStorageService


class FakeMinioClientBucketExists:
    """
    Fake MinIO client used to simulate an existing RAW bucket.

    This avoids requiring a real MinIO container during unit tests.
    """

    def bucket_exists(self, bucket_name: str) -> bool:
        return True

    def make_bucket(self, bucket_name: str) -> None:
        raise AssertionError("make_bucket should not be called when bucket exists")


class FakeMinioClientBucketMissing:
    """
    Fake MinIO client used to simulate a missing RAW bucket.

    The service should create the bucket when it does not exist.
    """

    def __init__(self) -> None:
        self.created_bucket = None

    def bucket_exists(self, bucket_name: str) -> bool:
        return False

    def make_bucket(self, bucket_name: str) -> None:
        self.created_bucket = bucket_name


class FakeMinioClientConnectionError:
    """
    Fake MinIO client used to simulate a storage connection error.

    This validates that the service returns a controlled error response instead
    of crashing the API.
    """

    def bucket_exists(self, bucket_name: str) -> bool:
        raise Exception("Connection failed")


def test_storage_health_returns_ok_when_raw_bucket_exists() -> None:
    """
    The storage service should report OK when the RAW bucket already exists.
    """
    service = ObjectStorageService(client=FakeMinioClientBucketExists())

    result = service.ensure_raw_bucket_exists()

    assert result.status == "ok"
    assert result.bucket == "raw"
    assert result.available is True
    assert result.message == "RAW bucket already exists."


def test_storage_health_creates_raw_bucket_when_missing() -> None:
    """
    The storage service should create the RAW bucket when it does not exist.
    """
    fake_client = FakeMinioClientBucketMissing()
    service = ObjectStorageService(client=fake_client)

    result = service.ensure_raw_bucket_exists()

    assert result.status == "created"
    assert result.bucket == "raw"
    assert result.available is True
    assert result.message == "RAW bucket was created successfully."
    assert fake_client.created_bucket == "raw"


def test_storage_health_returns_error_when_connection_fails() -> None:
    """
    The storage service should return a controlled error when MinIO is not reachable.
    """
    service = ObjectStorageService(client=FakeMinioClientConnectionError())

    result = service.ensure_raw_bucket_exists()

    assert result.status == "error"
    assert result.bucket == "raw"
    assert result.available is False
    assert "Connection failed" in result.message
