# function declaration
def greet():
    print(f'welcome ajs,good afternoon')

greet()
# functions with arguments
def greet1(name):
    '''
    hello this is a simple function
    which takes name as argument and
    greets that person!
    '''
    print(f'hey {name}')

greet1('ajs')

# doc strings used just for documentation
print(greet1.__doc__)

# function with return statement
def appendString(name):
    return f"{name} appended"

print(appendString("ajs"))

# scopes of variable in function
def add(a,b):
    sum = 0
    if a > 0 and b > 0:
        sum = a + b
        return sum
    else:
        return "values are either zero or negative"

sum = 10 
print(add(-2,3))
print(sum)

