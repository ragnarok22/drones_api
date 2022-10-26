from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models
from .constants import DroneState
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

    @action(detail=False)
    def available(self, request, *args, **kwargs):
        drones = models.Drone.objects.filter(state=DroneState.IDLE.value)
        return Response(DroneSerializer(drones, many=True).data)

    @action(detail=True)
    def battery(self, request, *args, **kwargs):
        drone = self.get_object()
        return Response(DroneSerializer(drone).data.get("battery_capacity"))


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = models.Medication.objects.all()
    serializer_class = MedicationSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
