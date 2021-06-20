# there are 3 types of functions arguments support in python
# they are default, positional and keywords

# positional arguments
def greet(name, msg):
    print(F'''hello {name}
{msg}
''')

greet('ajs','you have got n notifications')

# keyword arguments
# we should specify which value prompts to which keywords
# for example
def power(value, power):
    return (value ** power)

print(power(power = 2,value = 10))
# we can change the order when we specify the keyword arguments
# we can mix it
print(power(10, power = 3))

# default arguments
def power(value = 1, power = 1):
    return (value ** power)

print(power())
print(power(10))
print(power(power=8))
print(power(10,2))