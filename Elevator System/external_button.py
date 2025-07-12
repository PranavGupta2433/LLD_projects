from direction import Direction
from external_button_dispatcher import ExternalButtonDispatcher

class ExternalButtons:

    def __init__(self):
        self.external_dispatcher = ExternalButtonDispatcher()

    def press_button(self, floor, direction: Direction):
        print(f"External button press button {floor}, {direction}")
        self.external_dispatcher.submit_external_button_request(floor, direction)

