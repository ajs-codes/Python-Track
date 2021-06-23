# class variables (static for all instances)
class People:
    count = 0
    base_age = 18

    def __init__(self,name,age):
        self.name = name 
        self.age = age
        People.count += 1

    def validate(self):
        if self.age > People.base_age:
            return "you are valid"
        else:
            return "you are not valid"


        

user1 = People("ajs", 17)
user2 = People("sairam",20)
print(user1.__dict__)
print(user2.validate())
    