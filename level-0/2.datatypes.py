# datatypes in python
int = 30    #integer(whole numbers)
float = 3.44    #floating point numbers(decimal numbers)
string = "this is string"   #strings (character or sequence of characters)
boolean = True  #True or False value

print(int)
print(float)
print(string)
print(boolean)

# simple exercise

patient_name = input("enter your name : ")
patient_age = int(input("enter your age :"))
is_new_patient = bool(input("are you a new patient : (True or False) "))

print("hey",patient_name)
print("your age is",patient_age)
print("your arrival(new = True||old = False)",is_new_patient)
