from __future__ import annotations
from typing import List
from enum import Enum
import heapq


class Elevator_state(Enum):
     IDLE = 0
     MOVING = 1


class Direction(Enum):

    UP = 1
    DOWN = -1
    IDLE = 0

class Building:

    def __init__(self, floors: List[Floor]):
        self.floors_list : List[Floor] = floors
    
    def add_floor(self, new_floor: Floor):
        self.floors_list.append(new_floor)

    def remove_floor(self, remove_floor: Floor):
        self.floors_list.remove(remove_floor)

    def get_all_floors(self) -> List[Floor]:
        return self.floors_list


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

class InternalButtonDispatcher:

    def __init__(self):
        self.elevator_controller_list: List[ElevatorController] = Elevator_creator.elevator_controller_list
    

    def submit_internal_button_request(self, floor, elevator_car):
        for controller in self.elevator_controller_list:
            if controller.elevator_car == elevator_car:
                controller.submit_internal_Request(floor)
                break

class Floor:

    def __init__(self, floor: int):
        self.floor = floor
        self.external_button = ExternalButtons()

    def press_button(self, direction : Direction):
        self.external_button.press_button(self.floor, direction)

class ExternalButtons:

    def __init__(self):
        self.external_dispatcher = ExternalButtonDispatcher()

    def press_button(self, floor, direction: Direction):
        print(f"External button press button {floor}, {direction}")
        self.external_dispatcher.submit_external_button_request(floor, direction)

class ExternalButtonDispatcher:

   def __init__(self):
        self.elevator_controller_list : list[ElevatorController] = Elevator_creator.elevator_controller_list


   def submit_external_button_request(self, floor, direction: Direction):
       for controller in self.elevator_controller_list:
        #    print(f"cotroller list : {self.elevator_controller_list}")
        #    print(f"Going in elevator id : {controller.elevator_car.elevator_id}, floor: {floor},  {direction}")
           elevatorId = controller.elevator_car.elevator_id 
           if elevatorId%2 == 1 and floor %2 ==1:    #( for odd)
               print(f"lift id {elevatorId} will come to reach floor {floor} with direction {direction}")
               controller.submit_external_request(floor, direction)
               

           elif elevatorId%2 == 0 and floor %2 ==0:    #( for even)
               print(f"lift id {elevatorId} will come")
               controller.submit_external_request(floor, direction)
               



class ElevatorController:
    def __init__(self, elevator_car : Elevator_car):
        self.elevator_car = elevator_car
        self.up_min_pq = []   # min heap to handle upward requests
        self.down_max_pq = []   # max heap to handle downward requests  ( store negative values as heapq function supports only min heap)

    def submit_external_request(self, floor, direction: Direction):

        if direction == Direction.DOWN:    # ( use max heap)
            heapq.heappush(self.down_max_pq, -floor)
            # print(self.down_max_pq)
            self.control_elevator() 
            
            
        else:  # ( use min heap)
            heapq.heappush(self.up_min_pq, floor) 
            # print(self.up_min_pq)
            self.control_elevator() 

                  
        

    def submit_internal_Request(self, floor: int):
        current_floor = self.elevator_car.current_floor
        if floor > current_floor:
            current_dir = Direction.UP
        elif floor <  current_floor:
            current_dir = Direction.DOWN
        else:
            print(f"You are at floor {floor}")
            return
        # current_dir = self.elevator_car.direction
        self.submit_external_request(floor, current_dir)

    def control_elevator(self):
        
        if self.up_min_pq:
            self.elevator_car.direction = Direction.UP
        elif self.down_max_pq:
            self.elevator_car.direction = Direction.DOWN

        # print(f"Program in control_elevator function with direction = {self.elevator_car.direction} and up_min_pq = {self.up_min_pq} and down_max_pq = {self.down_max_pq}")

        while True:

            if self.elevator_car.direction == Direction.UP and self.up_min_pq:
                next_floor = heapq.heappop(self.up_min_pq)
                if self.elevator_car.current_floor < next_floor:
                    self.elevator_car.move_elevator(Direction.UP, next_floor)
                elif self.elevator_car.current_floor > next_floor:
                    self.elevator_car.move_elevator(Direction.DOWN, next_floor)
                else:
                    print(f"Already at floor {next_floor}")


            elif self.elevator_car.direction == Direction.DOWN and self.down_max_pq:
                next_floor = -heapq.heappop(self.down_max_pq)
                if self.elevator_car.current_floor < next_floor:
                    self.elevator_car.move_elevator(Direction.UP, next_floor)
                elif self.elevator_car.current_floor > next_floor:
                    self.elevator_car.move_elevator(Direction.DOWN, next_floor)
                else:
                    print(f"Already at floor {next_floor}")



            else:
                break

class Elevator_car:

    def __init__(self, elevator_id):

        self.elevator_id = elevator_id
        self.display = Display()
        # self.internalbuttons = InternalButtons()
        
        self.elevator_state = Elevator_state.IDLE
        self.direction = Direction.UP
        self.current_floor = 0

    def show_display_while_moving(self):
        return self.display.show_display()
    
    def press_button(self, destination):
        InternalButtons().press_button(destination, self)
        # self.internalbuttons.press_button(destination, self)

    def set_display_while_moving(self):
        return self.display.set_display(self.current_floor, self.direction)
    
    def move_elevator(self, direction: Direction, dest_floor):
        # try:
        #     direction = Direction[direction.upper()]
        # except KeyError:
        #     raise ValueError("Direction must be 'UP' or 'DOWN'")
        
        start_floor = self.current_floor
        print(f"start floor : {start_floor}, dest floor : {dest_floor}, direction : {self.direction}")

        if direction == Direction.UP:
            for floor in range(start_floor, dest_floor+1):
                self.current_floor = floor
                self.set_display_while_moving()
                self.show_display_while_moving()
                if floor == dest_floor:
                    print(f"Reached to floor : {self.current_floor}")
                    return True
                
        elif direction == Direction.DOWN:
            for floor in range(start_floor, dest_floor-1, -1):
                self.current_floor = floor
                self.set_display_while_moving()
                self.show_display_while_moving()
                if floor == dest_floor:
                    return True
                
        return False
    
class Display:

    def __init__(self):

        self.floor = None
        self.direction = None

    def set_display(self, floor, direction):

        if isinstance(direction, str):
            try:
                self.direction = Direction[direction.upper()]
            except KeyError:
                raise ValueError("Direction must be UP or DOWN")
        elif isinstance(direction, Direction):
            self.direction = direction
            
        self.floor = floor
        # self.direction = Direction[direction]
    
    def show_display(self):
        print(f"Current floor : {self.floor}")
        print(f"Current Direction : {self.direction.name}")

class Elevator_creator:

    elevator_controller_list : list[ElevatorController] = []

    @classmethod
    def initialize_elevator(cls):
        for i in range(1,3):  # creating elevator with id's 1 and 2
            elevator_car = Elevator_car(i)
            controller = ElevatorController(elevator_car)
            cls.elevator_controller_list.append(controller)






def main():


    Elevator_creator.initialize_elevator()
    floors_list = [Floor(i) for i in range(1, 6)]
    building = Building(floors_list)

    print("\n External requests:")

    building.get_all_floors()[1].press_button(Direction.UP)
    building.get_all_floors()[2].press_button(Direction.DOWN)
    building.get_all_floors()[3].press_button(Direction.DOWN)

    print("\n🛗 Internal request:")
    elevator1_controller = Elevator_creator.elevator_controller_list[0]   # taking elevator 1
    print(elevator1_controller.elevator_car.elevator_id)
    elevator1_controller.elevator_car.press_button(5)
    elevator1_controller.elevator_car.press_button(5)

    # print("\n Elevator movements:")
    # for controller in Elevator_creator.elevator_controller_list:
    #     controller.control_elevator()





if __name__ == "__main__":
    main()