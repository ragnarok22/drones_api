from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models
from .serializers import DroneSerializer, MedicationSerializer


class DroneViewSet(viewsets.ModelViewSet):
    queryset = models.Drone.objects.all()
    serializer_class = DroneSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=True)
    def medications(self, request, *args, **kwargs):
        drone = self.get_object()
        print(drone)
        return Response(DroneSerializer(drone).data.get("medications"))


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = models.Medication.objects.all()
    serializer_class = MedicationSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
