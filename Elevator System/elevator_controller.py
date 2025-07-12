from direction import Direction
from elevator_car import Elevator_car
import heapq

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


    
