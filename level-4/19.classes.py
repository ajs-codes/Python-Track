# object oriented programming
# declaration
class Myclass:
    pass

# instance of class
obj1 = Myclass()
print(obj1,type(obj1))

# properties/variables of instances
obj1.firstname = "kitty"
obj1.lastname = "cat"
obj1.species = "cat"
obj1.age = "9"

print(f"hello my name is {obj1.firstname} {obj1.lastname}, i am a {obj1.species}, and my age is {obj1.age}.")

# properties/variables of class using __init__() method(constructor)
class People:
    def __init__(self,firstname,lastname,age,gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
    

person1 = People("sharan", "aj", 20, "male")
print(person1.gender)

# class methods

class Employee:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"hey, i am {self.name}, i am {self.age} years old!")


emp1 = Employee("ajs", 20)
emp1.display()