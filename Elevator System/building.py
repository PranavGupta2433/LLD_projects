from typing import List
from floor import Floor

class Building:

    def __init__(self, floors: List[Floor]):
        self.floors_list : List[Floor] = floors
    
    def add_floor(self, new_floor: Floor):
        self.floors_list.append(new_floor)

    def remove_floor(self, remove_floor: Floor):
        self.floors_list.remove(remove_floor)

    def get_all_floors(self) -> List[Floor]:
        return self.floors_list



