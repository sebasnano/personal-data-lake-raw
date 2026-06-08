# Docker Local Development

## 1. Purpose

This document explains how to run the Personal Data Lake RAW API using Docker during development.

The goal of this setup is to provide a reproducible development environment without installing Python dependencies directly on the host machine.

---

## 2. Development vs Production Compose

The project includes two Docker Compose files:

| File | Purpose |
|---|---|
| `docker-compose.dev.yml` | Development mode with auto-reload and test dependencies |
| `docker-compose.yml` | Production-like mode without auto-reload |

---

## 3. Development Mode

Run the API in development mode:

```bash
docker compose -f docker-compose.dev.yml up --build
