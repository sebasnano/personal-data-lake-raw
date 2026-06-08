# Lightweight Python base image.
# Python 3.12 is used to match the current development runtime.
FROM python:3.12-slim

# Prevent Python from writing .pyc files and force logs to appear immediately.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Default working directory inside the container.
WORKDIR /code

# Allows the same Dockerfile to install production or development dependencies.
# Production uses requirements.txt.
# Development can use requirements-dev.txt from docker-compose.dev.yml.
ARG REQUIREMENTS_FILE=requirements.txt

# Copy dependency files first to improve Docker layer caching.
COPY requirements.txt requirements-dev.txt ./

# Install Python dependencies.
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r ${REQUIREMENTS_FILE}

# Copy the application source code.
COPY app ./app

# Create a non-root user for safer container execution.
RUN useradd --create-home --shell /bin/bash appuser

# Run the application as a non-root user.
USER appuser

# FastAPI will listen on port 8000 inside the container.
EXPOSE 8000

# Default production-like command.
# Development overrides this command to enable --reload.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
