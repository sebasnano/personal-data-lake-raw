# Roadmap

## 1. Overview

This roadmap defines the planned evolution of the Personal Data Lake RAW project.

The project will be developed in small and controlled phases. The first priority is to build a reliable RAW storage layer. Later phases will introduce metadata management, ETL pipelines, structured data models, queries, alerts, and dashboards.

---

## 2. Phase 1: API Foundation

### Goal

Create the initial FastAPI project structure and verify that the backend can run correctly.

### Scope

* Create project repository.
* Add initial documentation.
* Create FastAPI application.
* Add `/health` endpoint.
* Add environment configuration.
* Add Dockerfile.
* Add Docker Compose file.
* Prepare Coolify deployment.

### Expected Result

The API runs successfully and responds to health checks.

### Status

Planned.

---

## 3. Phase 2: Metadata Catalog

### Goal

Create the first version of the metadata catalog using PostgreSQL.

### Scope

* Add PostgreSQL service.
* Configure database connection.
* Create `raw_files` table.
* Register basic file metadata.
* Add database migrations or initialization scripts.
* Add basic repository/service layer.

### Expected Result

The system can store metadata records for raw files.

### Status

Planned.

---

## 4. Phase 3: Object Storage

### Goal

Integrate MinIO as the RAW object storage layer.

### Scope

* Add MinIO service.
* Create RAW bucket.
* Configure MinIO environment variables.
* Add storage service in the backend.
* Upload files to MinIO.
* Store object path in PostgreSQL.

### Expected Result

The system can store raw files in MinIO and keep metadata in PostgreSQL.

### Status

Planned.

---

## 5. Phase 4: File Ingestion

### Goal

Create the first complete ingestion flow.

### Scope

* Add `POST /files/upload`.
* Receive files from the API.
* Calculate SHA-256 hash.
* Detect duplicated files.
* Store new files in MinIO.
* Register metadata in PostgreSQL.
* Mark duplicated files correctly.
* Add basic error handling.

### Expected Result

A user can upload a file and the system stores it only if it is not duplicated.

### Status

Planned.

---

## 6. Phase 5: File Catalog API

### Goal

Expose endpoints to query the metadata catalog.

### Scope

* Add `GET /files`.
* Add `GET /files/{file_id}`.
* Add filters by domain, status, source, and file type.
* Return metadata without exposing sensitive storage credentials.

### Expected Result

A user can query which files exist in the RAW Data Lake.

### Status

Planned.

---

## 7. Phase 6: Basic Logs and Status Tracking

### Goal

Track ingestion events and file processing status.

### Scope

* Add ingestion logs.
* Register upload attempts.
* Register duplicate attempts.
* Register storage errors.
* Register processing status.
* Support statuses such as `pending`, `stored`, `duplicated`, `error`, `rejected`, and `processed`.

### Expected Result

The system can explain what happened during each file ingestion attempt.

### Status

Planned.

---

## 8. Phase 7: First ETL Prototype

### Goal

Create the first simple ETL process from RAW files into structured data.

### Scope

* Select one initial file type.
* Read data from RAW storage.
* Extract basic information.
* Save processed output.
* Mark RAW file as processed.
* Document the ETL flow.

### Expected Result

The system can process at least one type of raw file and produce structured output.

### Status

Future.

---

## 9. Phase 8: Structured Data Layer

### Goal

Create the first structured database layer for useful processed data.

### Scope

* Define first structured entities.
* Create database tables.
* Store processed records.
* Link processed data back to raw evidence.
* Keep traceability between RAW and structured data.

### Expected Result

The system can store useful processed information while preserving the original raw file reference.

### Status

Future.

---

## 10. Phase 9: Queries and Reports

### Goal

Create basic queries to extract value from processed data.

### Scope

* Add simple query endpoints.
* Add basic summaries.
* Add filters by date, domain, and source.
* Create first reporting outputs.

### Expected Result

The system can answer simple questions using processed data.

### Status

Future.

---

## 11. Phase 10: Alerts and Automation

### Goal

Add basic alerts based on processed information.

### Scope

* Detect pending items.
* Detect duplicated uploads.
* Detect failed processing.
* Detect upcoming renewals or payments in future financial modules.
* Prepare notification mechanisms.

### Expected Result

The system can identify important events without requiring manual review every time.

### Status

Future.

---

## 12. Phase 11: Dashboards

### Goal

Create visual dashboards for the information stored and processed by the system.

### Scope

* Add basic dashboard interface.
* Show file ingestion metrics.
* Show processing status.
* Show domain distribution.
* Later, add financial, productivity, knowledge, and infrastructure views.

### Expected Result

The system provides a visual overview of stored and processed information.

### Status

Future.

---

## 13. Long-Term Vision

The long-term goal is to evolve from a RAW Data Lake into a complete personal data platform.

Expected evolution:

```text
RAW Data Lake
      ↓
Metadata Catalog
      ↓
ETL Pipelines
      ↓
Structured Data Layer
      ↓
Queries and Reports
      ↓
Alerts and Automations
      ↓
Dashboards
      ↓
Personal Decision System
```

---

## 14. Development Strategy

The project should follow an incremental strategy:

* Build one small feature at a time.
* Keep each phase deployable.
* Document every important decision.
* Avoid adding advanced processing before the RAW layer is stable.
* Keep raw files traceable.
* Preserve evidence.
* Separate development, quality, and production environments when possible.

---

## 15. Current Priority

The current priority is:

```text
Phase 1: API Foundation
```

The immediate technical task is to create the FastAPI base application and validate it with the `/health` endpoint.
