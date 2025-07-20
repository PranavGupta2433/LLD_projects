from user import User
from store import Store
class VehicleRentalSystem:

    def __init__(self, stores : list[Store] = None, users: list[User]= None):

        self.stores = stores if stores else []
        self.users = users if users else []

    def get_store(self):
        return self.stores[0]

    