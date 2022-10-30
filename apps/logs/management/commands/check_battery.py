from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class Command(BaseCommand):
    help = "heck drones battery levels and create history/audit even log for this."

    def handle(self, *args, **options):
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=8,
            period=IntervalSchedule.HOURS
        )
        PeriodicTask.objects.get_or_create(
            interval=schedule,
            name="Check drones battery levels and create history/audit even log for this.",
            task="apps.logs.tasks.check_drone_battery_task"
        )
