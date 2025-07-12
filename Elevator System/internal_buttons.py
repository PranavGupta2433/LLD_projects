from Internal_button_dispatcher import InternalButtonDispatcher


class InternalButtons:
    
    def __init__(self):
        self.dispatcher = InternalButtonDispatcher()
        self.available_buttons = [1,2,3,4,5,6,7,8,9,10]
        self.button_selected = None

    def press_button(self, destination, elevator_car):

        if destination  not in self.available_buttons:
            raise ValueError(f"Floor {destination} is not available")
        else:

            self.button_selected = destination
            self.dispatcher.submit_internal_button_request(destination, elevator_car)
