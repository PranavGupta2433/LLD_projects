class User:

    def __init__(self, id, name, licence: bool):
        self.id = id
        self.name = name
        self.licence = licence

    def get_userinfo(self):
        return f"name = {self.name},  id = {self.id}"
    
    def has_licence(self):
        if self.licence:
            return True
        else:
            return False
    