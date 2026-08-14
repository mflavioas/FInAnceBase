import os
from celery import Celery

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "finknowledge_workers",
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=[
        "pipelines.ingestion.collector",
        "pipelines.normalization.parser",
        "pipelines.classification.classifier_agent"
    ]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)
