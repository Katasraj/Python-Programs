class Shape:
    def area(self):
        raise NotImplemented("Sub Class Should Implement")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(3.14*self.radius*self.radius)

c = Circle(5)
c.area()