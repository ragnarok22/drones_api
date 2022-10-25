from django.contrib import admin
from .models import Drone, Medication


@admin.register(Drone)
class DroneAdmin(admin.ModelAdmin):
    list_display = ("serial_number", "model", "battery_capacity", "state", "occupied_weight", "free_weight")
    list_filter = ("model", "state")


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ("name", "weight", "code", "drone_assigned")
    list_filter = ("drone_assigned",)
