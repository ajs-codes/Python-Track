# type conversion is useful,
# when you get data from a user,

# coz basically all the input comes as string
# for example
birth_year = int(input("enter your birth year to calculate age : "))
age = 2021 - birth_year
print(age,type(age))
# there are various type convertion function
# type(1 argument) to check the data type of that data or variable
num = int("445")
print(num,type(num))
decimal = float("43")
print(decimal,type(decimal))
boolean = bool("str")
print(boolean,type(boolean))
string = str(3452)
print(string,type(string))


