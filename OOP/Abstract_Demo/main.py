from abstract_class import Vehicle

class Bike(Vehicle):
    def __init__(self,n,color):
        super().__init__(n)
        self.color = color
    def start(self):
        print("Starts with Kick")

    def disply(self):
        print(f"My color is {self.color}")

class Scooty(Vehicle):
    def __init__(self,n):
        self.no_of_tyres = n
    def start(self):
        print("Self Start")

class Car(Vehicle):
    def __init__(self, n, x):
        super().__init__(n)
        self.gears = 6
    def start(self):
        print("Starts with Key")


