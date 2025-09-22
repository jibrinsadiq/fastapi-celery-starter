# fastapi-celery-starter

FastAPI + Celery template with JWT auth and Docker Compose (RabbitMQ). Good for ingestion/webhooks/inference services.

## Run in 2 minutes (Docker)
```bash
docker compose up --build
# API: http://localhost:8080/docs
# RabbitMQ UI: http://localhost:15672  (guest/guest)
