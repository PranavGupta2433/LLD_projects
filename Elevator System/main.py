from floor import Floor
from building import Building
from elevator_creator import Elevator_creator
from direction import Direction

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