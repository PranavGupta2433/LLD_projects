from location import Location
from VehicleInventory import VehicleInventory
# from Reservation import Reservation
from Vehicle import Vehicle
from user import User
from store import Store



v1 = Vehicle(1, "car")  
inventory = VehicleInventory()

inventory.add_vehicle(v1)

l1 = Location("sharda Sadan", "modinagar", "UP", "India", 201204)
s1 = Store(1, inventory, l1)

# print(s1.get_vehicles())
# s1.get_store_location() 

u1 = User(1, "Pranav", True)

s1.make_reservations(10, u1, v1)

# s1.complete_reservation(10)