from django.core.exceptions import ValidationError
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models
from .constants import DroneState
from .serializers import DroneSerializer, MedicationSerializer


class DroneViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for **Drones**.
    """
    queryset = models.Drone.objects.all()
    serializer_class = DroneSerializer

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = self.queryset

        model = self.request.query_params.get("model")
        if model:
            queryset = queryset.filter(model=model)

        battery_capacity = self.request.query_params.get("battery_capacity")
        if battery_capacity:
            queryset = queryset.filter(battery_capacity__gt=battery_capacity)

        state = self.request.query_params.get("state")
        if state:
            queryset = queryset.filter(state=state)

        return queryset

    @action(detail=True)
    def medications(self, request, *args, **kwargs):
        """Get the Drone's medications"""
        drone = self.get_object()
        serializer = self.get_serializer(drone)

        return Response(serializer.data.get("medications"))

    @action(detail=False)
    def available(self, request, *args, **kwargs):
        """Get the available drones. A available drone has IDLE status"""
        drones = models.Drone.objects.filter(state=DroneState.IDLE.value)
        serializer = self.get_serializer(drones, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def battery(self, request, *args, **kwargs):
        """Get the drone's battery"""
        drone = self.get_object()
        serializer = self.get_serializer(drone)
        return Response(serializer.data.get("battery_capacity"))

    @action(detail=True, methods=['POST'])
    def load(self, request, *args, **kwargs):
        """Load a drone with medications"""
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
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for **Users**.
    """
    queryset = models.Medication.objects.all()
    serializer_class = MedicationSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
