from celery import shared_task

@shared_task(name="tasks.echo")
def echo(user_id: str, message: str):
    return {"user": user_id, "+echo": message}