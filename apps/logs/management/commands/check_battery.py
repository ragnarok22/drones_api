from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class Command(BaseCommand):
    help = "heck drones battery levels and create history/audit even log for this."

    def add_arguments(self, parser):
        parser.add_argument(
            '--hour',
            help='Change the hours instead set 8 hours',
            type=int
        )

    def handle(self, *args, **options):
        hour = options['hour'] or 8

        schedule, created = IntervalSchedule.objects.get_or_create(
            every=hour,
            period=IntervalSchedule.HOURS
        )
        PeriodicTask.objects.get_or_create(
            interval=schedule,
            name=f"Check drones battery levels and create history/audit even log for this every {hour} hours.",
            task="apps.logs.tasks.check_drone_battery_task"
        )
        self.stdout.write(self.style.SUCCESS(f"Check drones battery every {hour}"))
