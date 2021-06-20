from functools import reduce
# simply lambas are short-cut or one-liner functions
# declaration
func1 = lambda: print('hello world')

func1()
# lamba with expression
add = lambda x,y: print(x+y)
sub = lambda x,y: print(x-y)
multi = lambda x,y: print(x*y)
divi = lambda x,y: print(x/y)
power = lambda x,y: print(x**y)

add(2,3)
sub(2,3)
multi(2,3)
divi(2,3)
power(2,3)

# lambda with higher order functions
# map,filter,reduce

# map
list1 = [1,2,3,4,5,6,7,8]
powers = map(lambda x: x**x,list1)
print(list(powers))
# filter
evens = filter(lambda a: (a%2 == 0),list1)
print(list(evens))
# reduce
print()