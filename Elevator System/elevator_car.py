from display import Display
from direction import Direction
# from elevator_state import Elevator_state
from internal_buttons import InternalButtons


class Elevator_car:

    def __init__(self, elevator_id):

        self.elevator_id = elevator_id
        self.display = Display()
        # self.internalbuttons = InternalButtons()
        
        # self.elevator_state = Elevator_state.IDLE
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
    
                
            







        



