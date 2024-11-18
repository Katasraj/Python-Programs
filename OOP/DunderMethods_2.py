from main_1 import adding


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person name {self.name} and age {self.age}"

    def __add__(self, other):
        if isinstance(other,Person):
            return self.age+other.age
        elif isinstance(other,int):
            return self.age+other
        else:
            raise TypeError("unsupported operand type(s) for +: 'int' and 'Person'")

    def __sub__(self, other):
        return self.age-other.age

    def __mul__(self, other):
        return self.age*other.age

    def __truediv__(self, other):
        return self.age/other.age

    def __floordiv__(self, other):
        return self.age//other.age

    def __mod__(self, other):
        return self.age%other.age

p1 = Person('abc',40)
p2 = Person('xyz',22)
p3 = Person('fgd',20)
print(p1)
print(p2)
print(p3)
total_age = p1+p2
subtract_age = p1-p2
print("Total Age: ",total_age)
print("Subtract Age: ",subtract_age)
print("Multiply Age: ",p1*p2)
print("Divide Age: ",p1/p2)
print("Divide Age-Floor: ",p1//p2)
print("Age Modulus: ",p1%p2)

print(100*'*')
'''Format the output to your specific needs'''
class ComplexNumber:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def __repr__(self):
        return f"ComplexNumber {self.real}+{self.img}j"

c = ComplexNumber(2,3)
print(c)

print(100*'*')

class Mylist:
    def __init__(self):
        self.list = []
    def append_2_list(self,*args):
        self.list.extend(args)
    def __str__(self):
        return f"List {self.list}, List length {len(self.list)}"

    ''' method in Python allows you to define how objects of your class can be accessed using indexing or slicing'''
    def __getitem__(self, item):
        return self.list[item]

    '''method in Python allows you to define how elements of your custom sequence-like objects can be assigned or modified'''
    def __setitem__(self, key, value):
        self.list[key] = value
        return self.list

    def __delitem__(self, key):
        del self.list[key]



l = Mylist()
l.append_2_list(1,2,3,4,5,6,7,8)
print(l)
print(l[1:4])
l[1] = 5
print("After replacing: ",l)
del l[1]
print("After deleting one value: ",l)

print(100*'*')

class Calculation:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __pow__(self, power):
        return self.a**power, self.b**power

    def __lt__(self, other):
        return self.a<other.b

n1 = Calculation(2,5)
n2 = Calculation(3,6)
n3 = Calculation(4,7)
print("Power 1: ",n1**3)
print("Power 2: ",n2**2)
print("Power 3: ",n3**1)

print(100*'*')

class Comparison:
    def __init__(self,a):
        self.a = a

    def __lt__(self, other):
        return self.a < other.a

    def __le__(self, other):
        return self.a <= other.a

    def __eq__(self, other):
        return self.a==other.a

    def __ne__(self, other):
        return self.a != other.a


comp1 = Comparison(7)
comp2 = Comparison(8)
print("Compare lt: ",comp1<comp2)
print("Compare lt: ",comp2<comp1)
print("Compare le: ",comp1<=comp2)
print("Compare le: ",comp2<=comp1)
comp3 = Comparison(10)
comp4 = Comparison(10)
print("Compare eq: ",comp3==comp4)
print("Compare eq: ",comp3==comp2)
print("Compare ne: ",comp3!=comp4)
print("Compare ne: ",comp3!=comp2)

print(100*'*')

class Mybool:
    def __init__(self,a):
        self.a = a

    def __bool__(self):
        return bool(self.a)

b = Mybool([1,2,3])
if b:
    print("Value is True")
else:
    print("Value is False")

print(100*'*')

class CallableObject:
    '''method in Python allows you to make objects callable, meaning you can treat them like functions.'''
    def __call__(self, *args, **kwargs):
        multiplier = kwargs.get('multiplier')
        for _ in args:
            m = _*multiplier
            print(_*multiplier)
cal = CallableObject()
cal(1,2,3,4,multiplier=2)



