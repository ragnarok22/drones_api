from django.db import models

from apps.drones import validators


class Drone(models.Model):
    serial_number = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    weight_limit = models.IntegerField()
    battery_capacity = models.IntegerField(default=100)
    state = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.serial_number} {self.model}"


class Medication(models.Model):
    name = models.CharField(max_length=255, validators=[validators.medication_name_validator])
    weight = models.FloatField()
    code = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.name
