from fastapi import FastAPI
from pydantic import BaseModel
from .celery_app import celery_app

app = FastAPI(title="fastapi-celery-starter")

class Ping(BaseModel):
    message: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/ping")
def ping(body: Ping):
    # In dev, we don't require auth; use a placeholder user id
    task = celery_app.send_task("tasks.echo", args=["anon", body.message])
    return {"queued": task.id}
