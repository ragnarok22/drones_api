from django.db import models

from apps.drones import validators
from apps.drones.constants import DRONE_MODELS_CHOICES, DRONE_STATE_CHOICES


class Drone(models.Model):
    serial_number = models.CharField(max_length=100)
    model = models.CharField(max_length=100, choices=DRONE_MODELS_CHOICES)
    weight_limit = models.IntegerField(validators=[validators.weight_limit_validator])
    battery_capacity = models.IntegerField(default=100)
    state = models.CharField(max_length=50, choices=DRONE_STATE_CHOICES)

    def __str__(self):
        return f"{self.serial_number} {self.model}"


class Medication(models.Model):
    name = models.CharField(max_length=255, validators=[validators.medication_name_validator])
    weight = models.FloatField()
    code = models.CharField(max_length=255, validators=[validators.medication_code_validator])
    image = models.ImageField()

    def __str__(self):
        return self.name
