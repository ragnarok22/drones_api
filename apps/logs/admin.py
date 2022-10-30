from django.contrib import admin

from .models import Log


@admin.register(Log)
class DroneAdmin(admin.ModelAdmin):
    list_display = ("message", "created_at", "updated_at")

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
