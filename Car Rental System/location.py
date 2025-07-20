class Location:

    def __init__(self, address, city, state, country, pincode):
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.pincode = pincode

    def get_address(self):
        print(f"Address : {self.address}, {self.city}, {self.state}, {self.country}, {self.pincode}")