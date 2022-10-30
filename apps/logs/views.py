from rest_framework import viewsets

from . import models
from .serializers import LogSerializer


class LogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LogSerializer
    queryset = models.Log.objects.all()
