from django.core.exceptions import ValidationError
from rest_framework import viewsets, status
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
        serializer = self.get_serializer(drone)

        return Response(serializer.data.get("medications"))

    @action(detail=False)
    def available(self, request, *args, **kwargs):
        drones = models.Drone.objects.filter(state=DroneState.IDLE.value)
        serializer = self.get_serializer(drones, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def battery(self, request, *args, **kwargs):
        drone = self.get_object()
        serializer = self.get_serializer(drone)
        return Response(serializer.data.get("battery_capacity"))

    @action(detail=True, methods=['POST'])
    def load(self, request, *args, **kwargs):
        drone = self.get_object()
        medications_id = request.data.get("medications")
        if medications_id:
            medications = models.Medication.objects.filter(pk__in=medications_id)

            try:
                drone.load_medications(medications)
                return Response({"status": "success"}, status=status.HTTP_200_OK)
            except ValidationError as e:
                return Response(e, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"medications": ["This filed is required."]}, status=status.HTTP_400_BAD_REQUEST)


class MedicationViewSet(viewsets.ModelViewSet):
    queryset = models.Medication.objects.all()
    serializer_class = MedicationSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
