class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} sounds as {self.sound}")


class Dog(Animal):
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound



d = Dog('Rocky',"Bow...")
d.make_sound()