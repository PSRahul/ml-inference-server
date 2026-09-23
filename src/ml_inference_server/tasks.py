from celery import Celery

app = Celery(main="tasks", broker="redis://localhost:6379/0")
