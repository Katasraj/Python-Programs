class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age= age
        self.address = address

    def __getitem__(self, item):
        return item.name, item.age, item.address

    def __setitem__(self, key, value):
        if key == 'address':
            self.address = value
        elif key == 'name':
            self.name = value
        elif key == 'age':
            self.age = value
        else:
            raise KeyError("Invalid Attribute Name")




p = Person('abc',40,'Hyderabad')
print(f"Person details are name {p.name} age {p.age} and address {p.address}")
p['address'] = 'Chennai'
p['name'] = 'xyz'
p['age'] = 50
print("After setting")
print(f"Person details are name {p.name} age {p.age} and address {p.address}")

