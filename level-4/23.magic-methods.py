# magic methods in python(dunder methods)
# for example
class Class1:
    def __init__(self, name):
        self.name = name

# this special __init__ method used to intialize properties to object
# __repr__ and __str__ methods
class Person:
    def __init__(self, name):
        self.name = name
    # this will display when you call only object
    def __repr__(self):
        return "hello you have called a instance"
    # this will display when you call only object(it has higher priority)
    def __str__(self):
        return f"your name is {self.name}"

person1 = Person("ajs")
print(person1)
print(repr(person1))
print(str(person1))

# another example using existing classes in python
# int and str class
print(int.__add__(1,2))
print(str.__add__("str","1"))
# we can call special methods like this

# other special methods
# using __add__ method
class Numbers:
    def __init__(self, no):
        self.number = no

    def __add__(self, other):
        return self.number + other.number

num1 = Numbers(20)
num2 = Numbers(2)

print(num1 + num2)
# this is the implementation of addition operator
# these are also known as operator overloading


