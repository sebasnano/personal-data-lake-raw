from dataclasses import dataclass

from minio import Minio
from minio.error import S3Error

from app.config import get_settings


@dataclass
class StorageHealth:
    """
    Represents the current status of the RAW object storage layer.
    """

    status: str
    bucket: str
    available: bool
    message: str


class ObjectStorageService:
    """
    Service responsible for interacting with the RAW object storage layer.

    At this stage, the service only validates connectivity and ensures that the
    RAW bucket exists. File upload will be implemented in a future feature.
    """

    def __init__(self, client: Minio) -> None:
        self.client = client
        self.settings = get_settings()

    def ensure_raw_bucket_exists(self) -> StorageHealth:
        """
        Validate MinIO connectivity and create the RAW bucket if it does not exist.

        This method is intentionally small and explicit because it is the first
        integration point between the API and the Data Lake storage layer.
        """
        bucket_name = self.settings.minio_bucket_raw

        try:
            bucket_exists = self.client.bucket_exists(bucket_name)

            if not bucket_exists:
                self.client.make_bucket(bucket_name)

                return StorageHealth(
                    status="created",
                    bucket=bucket_name,
                    available=True,
                    message="RAW bucket was created successfully.",
                )

            return StorageHealth(
                status="ok",
                bucket=bucket_name,
                available=True,
                message="RAW bucket already exists.",
            )

        except S3Error as exc:
            return StorageHealth(
                status="error",
                bucket=bucket_name,
                available=False,
                message=f"MinIO S3 error: {exc.message}",
            )

        except Exception as exc:
            return StorageHealth(
                status="error",
                bucket=bucket_name,
                available=False,
                message=f"Unexpected storage error: {exc}",
            )
