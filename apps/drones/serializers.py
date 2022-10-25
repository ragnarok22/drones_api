from rest_framework import serializers

from .models import Drone, Medication


class MedicationSerializer(serializers.ModelSerializer):
    drone = serializers.ReadOnlyField(source='drone_assigned.model')

    class Meta:
        model = Medication
        fields = ["id", "name", "weight", "code", "image", "drone"]


class DroneSerializer(serializers.ModelSerializer):
    medications = MedicationSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Drone
        fields = ["id", "serial_number", "model", "weight_limit", "battery_capacity", "state", "medications"]
