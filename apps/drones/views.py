from rest_framework import generics, permissions

from .serializers import DroneSerializer, MedicationSerializer
from . import models


class DroneList(generics.ListCreateAPIView):
    queryset = models.Drone.objects.all()
    serializer_class = DroneSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Drone.objects.all()
    serializer_class = DroneSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MedicationList(generics.ListCreateAPIView):
    queryset = models.Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MedicationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Medication.objects.all()
    serializer_class = MedicationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
