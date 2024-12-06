class Human:
    def __init__(self,num_heart):
        self.no_of_eyes = 2
        self.no_of_nose = 1
        self.num_heart =num_heart

    def work(self):
        print("I can work")

    def eat(self):
        print("I can eat")


class Male(Human):
    def __init__(self,name,num_heart):
        self.name = name
        super().__init__(num_heart)

    def spaek(self):
        print("I can speak")

    def work(self):
        print("I can code")
        super().work()

    def display(self):
        print(f"Hi I am {self.name} and I have {self.num_heart} heart")


m = Male('Aakash',1)
m.work()
print(m.no_of_eyes)
m.display()