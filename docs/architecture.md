# Architecture

## 1. Overview

Personal Data Lake RAW is designed as the first storage layer for a personal data platform.

The system stores raw files without transforming them at ingestion time. Each file is cataloged with basic metadata, stored in an object storage service, and prepared for future ETL processes.

The main goal of this first version is not to clean or analyze the data yet. The goal is to create a reliable foundation for storing raw information from different personal domains such as finances, productivity, knowledge, and infrastructure.

---

## 2. High-Level Architecture

```text
Client / User
      ↓
FastAPI Backend
      ↓
Validation and Hash Calculation
      ↓
MinIO Object Storage
      ↓
PostgreSQL Metadata Catalog
      ↓
Future ETL Processes
      ↓
Structured Data, Dashboards and Automations
```

---

## 3. Main Components

### FastAPI Backend

The backend exposes the API endpoints used to interact with the system.

Initial responsibilities:

* Provide a health check endpoint.
* Receive files in future versions.
* Validate incoming data.
* Calculate file hashes.
* Store files in MinIO.
* Register metadata in PostgreSQL.

---

### MinIO Object Storage

MinIO is used as the RAW storage layer.

It stores the original files exactly as they are received, without applying transformations.

Examples of files that may be stored:

* CSV files.
* Excel files.
* PDF files.
* JSON files.
* TXT files.
* Screenshots.
* Logs.
* Exported reports.
* Manual evidence files.

---

### PostgreSQL Metadata Catalog

PostgreSQL stores the metadata catalog of the files stored in the Data Lake.

The catalog allows the system to know:

* Which files were uploaded.
* Where each file is stored.
* What type of file it is.
* Which domain it belongs to.
* Whether it was already processed.
* Whether it is duplicated.
* Whether an error occurred.

---

### Coolify

Coolify is used to deploy and manage the application stack on a VPS.

It provides a self-hosted deployment environment for:

* Backend services.
* Databases.
* Object storage.
* Environment variables.
* Application deployments.
* Future quality and production environments.

---

## 4. Data Flow

The expected data flow is:

```text
1. A file is received by the API.
2. The backend validates the file.
3. The backend calculates the SHA-256 hash.
4. The system checks if the file already exists.
5. If the file is new, it is stored in MinIO.
6. Metadata is registered in PostgreSQL.
7. The file remains available for future ETL processing.
```

---

## 5. Initial Storage Zones

The Data Lake will follow a simple zone-based structure.

```text
raw/
processed/
rejected/
logs/
metadata/
```

### RAW Zone

Stores original files without transformation.

### Processed Zone

Will store files or outputs that have already been processed by future ETL jobs.

### Rejected Zone

Will store files that could not be processed or did not meet minimum validation rules.

### Logs Zone

Stores execution logs, processing logs, and system events.

### Metadata Zone

Contains metadata references and catalog-related information.

---

## 6. Initial Domains

The system will organize raw information into the following domains:

### Finances

Financial files, transactions, statements, payment evidence, budgets, and investment-related information.

### Productivity

Tasks, routines, habits, events, reminders, and planning-related information.

### Knowledge

Notes, documents, resources, links, study material, and personal knowledge references.

### Infrastructure

VPS information, service logs, access records, incidents, renewals, and technical evidence.

### Unknown

Files that cannot be classified yet but may be useful in the future.

---

## 7. Duplicate Detection

The first duplicate detection strategy will be based on file hashing.

The backend will calculate a SHA-256 hash for each uploaded file.

If another file with the same hash already exists, the system should mark the new upload attempt as duplicated instead of storing it as a valid new file.

---

## 8. Initial File Statuses

Files may have the following statuses:

* `pending`
* `stored`
* `duplicated`
* `error`
* `rejected`
* `processed`

These statuses describe the file lifecycle inside the Data Lake, not the business meaning of the file content.

---

## 9. MVP Scope

The first version includes:

* FastAPI backend.
* Health check endpoint.
* Docker support.
* Coolify deployment support.
* MinIO integration preparation.
* PostgreSQL integration preparation.
* Basic project documentation.

Future versions will include:

* File upload endpoint.
* Metadata catalog table.
* MinIO file storage.
* Duplicate validation.
* Basic file listing.
* ETL pipelines.
* Dashboards.
* Alerts.
* Structured data models.

---

## 10. Out of Scope

The following features are not part of the initial architecture:

* Financial data processing.
* Budget calculation.
* Bank integrations.
* OCR.
* Artificial intelligence.
* Automatic email reading.
* Advanced dashboards.
* Full ETL pipelines.
* Predictive analytics.
* Final relational business model.

---

## 11. Future Evolution

The architecture is designed to evolve in small steps.

Planned evolution:

```text
RAW Data Lake
      ↓
Metadata Catalog
      ↓
Basic ETL Pipelines
      ↓
Structured Data Models
      ↓
Queries and Reports
      ↓
Dashboards
      ↓
Alerts and Automations
```

The first priority is to create a stable storage foundation. Once the RAW layer is working, future projects can focus on cleaning, transforming, analyzing, and visualizing the data.
