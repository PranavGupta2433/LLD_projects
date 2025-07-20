from ReservationStatus import ReservationStatus
from Vehicle import Vehicle
from user import User
# from VehicleInventory import VehicleInventory

class Reservation:

    def __init__(self):
        self.reservation_id = None
        self.user = None
        self.vehicle = None
        self.reservation_status: ReservationStatus = None

    def create_reservation(self, id, user: User, vehicle: Vehicle):
        self.reservation_id = id
        self.user = user
        self.vehicle = vehicle
        self.reservation_status = ReservationStatus.Scheduled

        print(f"Reservation has been scheduled for {self.user.get_userinfo()} and his Reservation id = {self.reservation_id}")

        return self.reservation_id

    
# inventory = VehicleInventory()
# v1 = Vehicle(1, "car")
# inventory.add_vehicle(v1)

# u1 = User(1, "Pranav", True)



