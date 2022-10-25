from django.db import models


class Drone(models.Model):
    serial_number = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    weight_limit = models.IntegerField()
    battery_capacity = models.IntegerField(default=100)
    state = models.CharField(max_length=50)


class Medication(models.Model):
    name = models.CharField(max_length=255)
    weight = models.FloatField()
    code = models.CharField(max_length=255)
    image = models.ImageField()
