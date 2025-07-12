from elevator_car import Elevator_car
from elevator_controller import ElevatorController

class Elevator_creator:

    elevator_controller_list : list[ElevatorController] = []

    @classmethod
    def initialize_elevator(cls):
        for i in range(1,3):  # creating elevator with id's 1 and 2
            elevator_car = Elevator_car(i)
            controller = ElevatorController(elevator_car)
            cls.elevator_controller_list.append(controller)