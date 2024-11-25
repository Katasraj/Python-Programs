class Student:
    def __init__(self,name,rollno,age):
        self.name = name          # Public Instance
        self._rollno = rollno     # Protected Instance
        self.__age = age          # Private Instance
    def __display(self):
        print(f"Hi my self {self.name}, roll no {self._rollno} and age {self.__age} from Student class")

    def displayPrivateData(self):
        self.__display()

class Branch(Student):
    def show(self):
        print(f"My roll no is {self._rollno}")
        '''print(f"My Age is {self.__age}")''' # Private attribute can't use in derived function

b1 = Branch('Rahul',50,40)
b1.displayPrivateData()
b1._rollno = 65
b1.__age = 35
b1.displayPrivateData()
b1.show()
print(100*'*')
s1 = Student('Rahul',23,20)
print(s1._Student__age)
