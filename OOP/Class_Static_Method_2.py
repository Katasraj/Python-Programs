class Student:

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def msg(self):
        print(self.name + ' got ' + self.marks,'%')

    @classmethod
    def get_per(cls,name,marks):
        return cls(name,str((int(marks)/600)*100))

    @staticmethod
    def get_age(age):
        if age < 16:
            print("Minor")
        else:
            print("Major")


s1 = Student('naga','85')
s1.msg()
s1.get_age(14)

S2 = Student.get_per('naga','560')
S2.msg()
S2.get_age(17)