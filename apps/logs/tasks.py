import celery

from apps.drones.models import Drone
from apps.logs.models import Log


@celery.shared_task
def check_drone_battery_task():
    drones_below_25 = Drone.objects.filter(battery_capacity__lt=25)
    drones_between_25_and_75 = Drone.objects.filter(battery_capacity__range=[25, 75])
    drones_more_than_75 = Drone.objects.filter(battery_capacity__gt=75)

    message = f"Battery Status:\n\n" \
              f"Below 25%:{drones_below_25} drones\n" \
              f"Between 25% and 75%: {drones_between_25_and_75} drones\n" \
              f"More than 75%: {drones_more_than_75}"

    log = Log.objects.create(message=message)
    return log
