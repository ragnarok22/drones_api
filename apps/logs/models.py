from django.db import models
from apps.core.models import TimeStampedModel


class Log(TimeStampedModel):
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.message
