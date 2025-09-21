import os
from celery import Celery


broker = os.getenv("BROKER_URL", "amqp://guest:guest@rabbitmq//")
backend = os.getenv("RESULT_BACKEND", None)


celery_app = Celery("fastapi-celery-starter", broker=broker, backend=backend)
celery_app.autodiscover_tasks(["app"]) # looks for app/tasks.py
