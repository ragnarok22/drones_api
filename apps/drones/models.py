from django.db import models

from apps.drones import validators
from apps.drones.constants import DRONE_MODELS_CHOICES, DRONE_STATE_CHOICES


class Drone(models.Model):
    serial_number = models.CharField(max_length=100)
    model = models.CharField(max_length=100, choices=DRONE_MODELS_CHOICES)
    weight_limit = models.IntegerField(validators=[validators.weight_limit_validator])
    battery_capacity = models.IntegerField(default=100)
    state = models.CharField(max_length=50, choices=DRONE_STATE_CHOICES)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.serial_number} {self.model}"

    def occupied_weight(self):
        weight = Medication.objects.filter(drone_assigned=self).aggregate(
            occupied_weight=models.Sum('weight')
        )["occupied_weight"]
        return weight if weight else 0

    def free_weight(self):
        return self.weight_limit - self.occupied_weight()


class Medication(models.Model):
    name = models.CharField(max_length=255, validators=[validators.medication_name_validator])
    weight = models.FloatField()
    code = models.CharField(max_length=255, validators=[validators.medication_code_validator])
    image = models.ImageField()
    drone_assigned = models.ForeignKey(Drone, null=True, blank=True, on_delete=models.DO_NOTHING,
                                       related_name="medications")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name
