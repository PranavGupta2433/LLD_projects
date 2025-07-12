from direction import Direction
from external_button import ExternalButtons

class Floor:

    def __init__(self, floor: int):
        self.floor = floor
        self.external_button = ExternalButtons()

    def press_button(self, direction : Direction):
        self.external_button.press_button(self.floor, direction)
