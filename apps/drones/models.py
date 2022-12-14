from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.drones import validators
from apps.drones.constants import DRONE_MODELS_CHOICES, DRONE_STATE_CHOICES, DroneState


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

    def load_medications(self, medications):
        total_weight = medications.aggregate(total_weight=models.Sum('weight'))['total_weight']
        if total_weight <= self.free_weight():
            medications.update(drone_assigned=self)
            self.state = DroneState.LOADING.value
            self.save()

        else:
            raise ValidationError(
                _('%(total_weight)dgr is too heavy for the Drone, only %(free_weight)dgr free.'),
                params={'total_weight': total_weight, "free_weight": self.free_weight()},
            )


class Medication(models.Model):
    name = models.CharField(max_length=255, validators=[validators.medication_name_validator])
    weight = models.FloatField()
    code = models.CharField(max_length=255, validators=[validators.medication_code_validator])
    image = models.ImageField(upload_to="medications/")
    drone_assigned = models.ForeignKey(Drone, null=True, blank=True, on_delete=models.DO_NOTHING,
                                       related_name="medications")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name
