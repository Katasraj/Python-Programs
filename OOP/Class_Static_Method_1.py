class Instructor:
    followers = 0

    def __init__(self,name,address):
        self.name = name
        self.address = address

    def display(self,subject_name):
        print(f"Hi I am {self.name} and I will teach {subject_name}")

    def update_followers(self,follower_name):
        self.followers += 1


Instructor_1 = Instructor('abc','hyd')
Instructor_1.display('python')
Instructor_1.update_followers('naga')
Instructor_1.update_followers('aaga')
print(Instructor_1.followers)

Instructor_2 = Instructor('ase','chennai')
Instructor_2.update_followers('maga')
print(Instructor_2.followers)


