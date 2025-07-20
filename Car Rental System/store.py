from location import Location
from VehicleInventory import VehicleInventory
from Reservation import Reservation
# from Vehicle import Vehicle
# from user import User

class Store:

    def __init__(self, store_id, vehicle_inventory: VehicleInventory, location: Location, reservation_list: Reservation= None):
        self.store_id = store_id
        self.vehicle_inventory = vehicle_inventory
        self.location = location
        self.reservation_list = reservation_list if reservation_list else []

    def get_vehicles(self):
        return self.vehicle_inventory.get_vehicles()
    
    def get_store_location(self):
        return self.location.get_address()
    
    def make_reservations(self, id, user, vehicle):
        reservation = Reservation()
        reservation.create_reservation(id, user, vehicle)
        self.reservation_list.append(reservation)

        return reservation
    
    # def complete_reservation(self, reservation_id):

    #    for reservation in self.reservation_list:
    #        print(f"Reservation completed for {reservation_id}")
    #        self.reservation_list.remove(reservation)
    

