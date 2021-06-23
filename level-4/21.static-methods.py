# class method
# declaration of class method 
class People:
    count = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        People.count += 1
    
    @classmethod
    def get_count(cls):
        print(cls.count)

person0 = People("ajs",18)
People.get_count()
person0.get_count()

# static methods
# static methods doesn't take self or class it behaves seperately
class Static:
    def isAdult(num):
        if num >= 18:
            return True
        else:
            return False
# we can access class method only using class not using objects
print(Static.isAdult(20))