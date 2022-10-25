from enum import Enum, auto


class DroneModel(Enum):
    Lightweight = "Lightweight"
    Middleweight = "Middleweight"
    Cruiserweight = "Cruiserweight"
    Heavyweight = "Heavyweight"


class DroneState(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    IDLE = auto()
    LOADING = auto()
    LOADED = auto()
    DELIVERING = auto()
    DELIVERED = auto()
    RETURNING = auto()


DRONE_MODELS_CHOICES = (
    (DroneModel.Lightweight.name, DroneModel.Lightweight.value),
    (DroneModel.Middleweight.name, DroneModel.Middleweight.value),
    (DroneModel.Cruiserweight.name, DroneModel.Cruiserweight.value),
    (DroneModel.Heavyweight.name, DroneModel.Heavyweight.value),
)

DRONE_STATE_CHOICES = (
    (DroneState.IDLE.name, DroneState.IDLE.value),
    (DroneState.LOADING.name, DroneState.LOADING.value),
    (DroneState.LOADED.name, DroneState.LOADED.value),
    (DroneState.DELIVERING.name, DroneState.DELIVERING.value),
    (DroneState.DELIVERED.name, DroneState.DELIVERED.value),
    (DroneState.RETURNING.name, DroneState.RETURNING.value),

)

