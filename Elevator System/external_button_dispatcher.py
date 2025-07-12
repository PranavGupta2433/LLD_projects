from direction import Direction
from elevator_creator import Elevator_creator
from elevator_controller import ElevatorController

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
               


    
       