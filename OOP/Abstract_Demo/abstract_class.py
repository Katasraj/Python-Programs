from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,n):
        self.no_of_tyres = n
    @abstractmethod
    def start(self):
        print("This is under abstaract class")

    def disply(self):
        print("I am calling from vehicle method")
