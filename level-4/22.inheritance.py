# inheritance is copy the methods and properties of one class to another
# for example
class baseclass():
    def get(self):
        print("this is base class")
    pass
class subclass(baseclass):
    def get_sub(self):
        print("this is subclass")
    pass


obj1 = subclass()
obj1.get()
obj1.get_sub()

# multiple inheritance
class base1:
    def get1(self):
        print("this is base one")

class base2:
    def get2(self):
        print("this is base two")

class subclass(base1, base2):
    def get_sub(self):
        base1.get1(self) 
        base2.get2(self)
        print("this is subclass")

person1 = subclass()
person1.get_sub()
person1.get1()
person1.get2()

# multilvl inheritance
class BaseClass:
    def base_method(self):
        print("this is base class")

class Sub1(BaseClass):
    def sub1(self):
        BaseClass.base_method(self)
        print("this is sub one class")

class Sub2(BaseClass):
    def sub2(self):
        BaseClass.base_method(self)
        print("this is sub two class")

print()
print()
obj1 = Sub1()
obj2 = Sub2()
obj1.sub1()
obj2.sub2()