# MVP Scope

## 1. Project Name

Personal Data Lake RAW

---

## 2. Purpose

The purpose of this MVP is to create the first storage layer for a personal data platform.

This first version focuses on storing raw files, cataloging them with basic metadata, and preparing the system for future ETL processes.

The project does not aim to clean, transform, analyze, or visualize the data yet. Its main goal is to provide a reliable foundation for future data processing.

---

## 3. Problem

Personal information is usually spread across different sources such as files, emails, screenshots, exports, logs, notes, financial records, and digital services.

Without a central storage layer, it becomes difficult to:

* Keep track of available information.
* Preserve original evidence.
* Avoid duplicated files.
* Prepare data for future processing.
* Build reliable ETL pipelines.
* Create dashboards or automations later.

---

## 4. MVP Goal

The MVP must provide a basic API that can be deployed with Docker and Coolify.

The system should be prepared to receive files, store them in a RAW storage layer, and register basic metadata in a catalog.

The first technical milestone is to build a working FastAPI service with a health check endpoint and a clean project structure.

---

## 5. Initial Scope

The MVP includes:

* FastAPI backend.
* Basic project structure.
* Health check endpoint.
* Dockerfile.
* Docker Compose support.
* Environment variable configuration.
* Initial documentation.
* Preparation for PostgreSQL integration.
* Preparation for MinIO integration.
* Coolify deployment support.

---

## 6. Future MVP Extensions

After the initial API base is working, the next extensions will include:

* File upload endpoint.
* SHA-256 file hash calculation.
* Duplicate detection.
* MinIO object storage integration.
* PostgreSQL metadata catalog.
* File listing endpoint.
* File detail endpoint.
* Basic ingestion logs.

---

## 7. Out of Scope

The following features are not part of the first MVP:

* Financial processing.
* Budget calculation.
* Bank integrations.
* Automatic email reading.
* OCR.
* Artificial intelligence.
* Advanced ETL pipelines.
* Data cleaning.
* Dashboards.
* Alerts.
* User authentication.
* Final business data model.
* Production-grade monitoring.

---

## 8. Main Use Case

The first expected use case is:

```text
A user uploads or provides a raw file.
The system calculates its hash.
The system checks whether the file already exists.
If the file is new, it is stored in the RAW zone.
The system registers metadata about the file.
The file becomes available for future ETL processing.
```

---

## 9. Initial Domains

The system should support raw information from the following domains:

* Finances.
* Productivity.
* Knowledge.
* Infrastructure.
* Unknown.

The `unknown` domain is used when the file cannot be classified yet but may still be useful later.

---

## 10. Success Criteria

The first MVP is considered successful when:

* The FastAPI application starts correctly.
* The `/health` endpoint responds successfully.
* The project can run with Docker.
* The project has a clear folder structure.
* The repository includes basic documentation.
* The application is ready to be deployed with Coolify.
* The codebase is prepared for PostgreSQL and MinIO integration.

---

## 11. First Deliverable

The first deliverable is a working API base.

Expected endpoint:

```http
GET /health
```

Expected response:

```json
{
  "status": "ok",
  "service": "personal-data-lake-api",
  "environment": "development"
}
```

---

## 12. Technical Stack

| Component                | Technology     |
| ------------------------ | -------------- |
| Backend                  | FastAPI        |
| Language                 | Python         |
| API Server               | Uvicorn        |
| Containerization         | Docker         |
| Local Orchestration      | Docker Compose |
| Deployment               | Coolify        |
| Future Metadata Database | PostgreSQL     |
| Future Object Storage    | MinIO          |

---

## 13. MVP Principle

The project should grow incrementally.

The first version must stay small and focused.
The priority is to create a solid technical foundation before adding business logic, dashboards, automation, or advanced data processing.
