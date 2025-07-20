from abc import ABC, abstractmethod

class ATM_Dispenser(ABC):

    
    def __init__(self, next_handeler= None):
        self.next_handeler = next_handeler

    def set_next_handeler(self, next_handeler):
        self.next_handeler = next_handeler

    @abstractmethod
    def dispense(self, amount):
        pass


class ThousandHandeler(ATM_Dispenser):

    def dispense(self, amount):
        if amount >= 1000:
            notes = amount // 1000
            remaining_amount = amount % 1000
            print(f"Dispensing {notes} notes of Rs 1000")
            if remaining_amount > 0 and self.next_handeler:
                self.next_handeler.dispense(remaining_amount)


        elif self.next_handeler:
            self.next_handeler.dispense(amount)

class FiveHundredHandeler(ATM_Dispenser):

    def dispense(self, amount):
        if amount >= 500:
            notes = amount // 500
            remaining_amount = amount % 500
            print(f"Dispensing {notes} notes of Rs 500")
            if remaining_amount > 0 and self.next_handeler:
                self.next_handeler.dispense(remaining_amount)


        elif self.next_handeler:
            self.next_handeler.dispense(amount)

class HundredHandeler(ATM_Dispenser):

    def dispense(self, amount):
        if amount >= 100:
            notes = amount // 100
            remaining_amount = amount % 100
            print(f"Dispensing {notes} notes of Rs 100")
            if remaining_amount > 0 and self.next_handeler:
                self.next_handeler.dispense(remaining_amount)


        elif self.next_handeler:
            self.next_handeler.dispense(amount)

class ATMDispenser:
    def __init__(self):
        # Initialize the chain of responsibility
        self.handler1000 = ThousandHandeler()
        self.handler500 = FiveHundredHandeler()
        self.handler100 = HundredHandeler()
        

        self.handler1000.set_next_handeler(self.handler500)
        self.handler500.set_next_handeler(self.handler100)

    def withdraw(self, amount):
        if amount % 100 != 0: # Assuming minimum denomination is 100
            print("Amount must be a multiple of 100.")
            return
        print(f"\nAttempting to withdraw: {amount}")
        self.handler1000.dispense(amount)



atm1 = ATMDispenser()
atm1.withdraw(5600)
