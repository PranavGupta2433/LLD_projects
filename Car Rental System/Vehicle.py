from VehicleType import VehicleType
from status import Status
class Vehicle:
    
    def __init__(self, vehicle_id: int, vehicle_type :VehicleType ):
        self. vehicle_id =vehicle_id
        self.vehicle_type = vehicle_type
        self.daily_rental_cost = None
        self.no_of_seat = None
        self.status = Status.Active

    def get_vehicle_id(self):
        return self.vehicle_id
    
    def set_vehicle_id(self, vehicle_id):
        self.vehicle_id = vehicle_id

    def get_vehicle_type(self):
        return self.vehicle_type
    
    def set_vehicle_type(self, vehicle_type: VehicleType):
        self.vehicle_type = vehicle_type

    def get_daily_rental_cost(self):
        return self.daily_rental_cost
    
    def set_daily_rental_cost(self, daily_rental_cost):
        self.daily_rental_cost = daily_rental_cost

    def get_no_of_seats(self):
        return self.no_of_seat
    
    def set_no_of_seats(self, seats):
        self.no_of_seat= seats

    def get_vehicle_status(self):
        return self.status
    
    def set_vehicle_status(self, status : Status):
        self.status = status

    

v1 = Vehicle(1, "car")
# v1.set_vehicle_status(Status.Inactive)
# print(v1.get_vehicle_status().value)

# v1.set_no_of_seats(2)
# v1.set_vehicle_status(Status.Active)

# print(v1.get_no_of_seats(), v1.get_vehicle_status())