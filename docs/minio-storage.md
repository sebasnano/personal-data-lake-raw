# MinIO RAW Object Storage

## 1. Purpose

MinIO is used as the RAW object storage layer for the Personal Data Lake.

The RAW storage layer keeps original files exactly as they are received. Files are not transformed at ingestion time. Future ETL processes will read from this storage layer and generate structured data later.

---

## 2. Why Object Storage

Object storage is a good fit for RAW data because it can store different file formats without forcing a relational structure from the beginning.

Examples of supported RAW files:

- CSV files.
- Excel files.
- PDF files.
- JSON files.
- TXT files.
- Screenshots.
- Logs.
- Exported reports.
- Manual evidence files.

---

## 3. Local Development Service

MinIO is included in Docker Compose as a local development service.

Service name:

```text
minio
