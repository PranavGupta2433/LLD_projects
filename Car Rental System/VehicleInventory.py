from Vehicle import Vehicle

class VehicleInventory:

    def __init__(self, vehicles_list: list = None):
        self.vehicles_list = vehicles_list if vehicles_list else []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles_list.append(vehicle)

    def get_vehicles(self):
        return self.vehicles_list
    
# inventory = VehicleInventory()
# v1 = Vehicle(1, "car")
# inventory.add_vehicle(v1)
# print(inventory.get_vehicles())