from enum import Enum

class ReservationStatus(Enum):

    Completed = "Completed"
    Scheduled = "scheduled"
    Canceled = "Canceled"
    