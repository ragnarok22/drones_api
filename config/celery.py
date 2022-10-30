import logging
import os

from celery import Celery
from django.conf import settings

logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.develop")

app = Celery("Drone-API")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

logger.debug(f"Celery conf: {app.conf}")
