from rest_framework import viewsets, permissions

from .serializers import DroneSerializer, MedicationSerializer
from . import models


class DroneViewSet(viewsets.ModelViewSet):
    queryset = models.Drone.objects.all()
    serializer_class = DroneSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = models.Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
