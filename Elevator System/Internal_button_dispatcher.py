from elevator_controller import ElevatorController
from elevator_creator import Elevator_creator
from typing import List

class InternalButtonDispatcher:

    def __init__(self):
        self.elevator_controller_list: List[ElevatorController] = Elevator_creator.elevator_controller_list
    

    def submit_internal_button_request(self, floor, elevator_car):
        for controller in self.elevator_controller_list:
            if controller.elevator_car == elevator_car:
                controller.submit_internal_Request(floor)
                break

        