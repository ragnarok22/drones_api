from rest_framework import serializers

from .constants import DroneState
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
        fields = ["id", "serial_number", "model", "weight_limit", "free_weight", "occupied_weight", "battery_capacity",
                  "state", "medications"]

    def validate(self, data):
        if data['battery_capacity'] < 25 and data['state'] == DroneState.LOADING.value:
            raise serializers.ValidationError({
                "state": "You can't loading the Drone because battery is lower than 25"
            })
        else:
            return data
