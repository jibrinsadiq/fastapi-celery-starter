from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from .auth import get_current_user
from .celery_app import celery_app


app = FastAPI(title="fastapi-celery-starter")


class Ping(BaseModel):
message: str


@app.get("/health")
def health():
return {"ok": True}


@app.post("/ping")
def ping(body: Ping, user=Depends(get_current_user)):
task = celery_app.send_task("tasks.echo", args=[user["sub"], body.message])
return {"queued": task.id}
