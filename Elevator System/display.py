from direction import Direction

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

# d = Display()
# d.set_display(1, Direction.UP)
# d.show_display()