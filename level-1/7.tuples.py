# tuples are similar to list but 
# they are immutable

# creating a tuple
tuple1 = (1,[1,2,3],"hello",{"one": "sharan"})
print(tuple1)
# we can enter all valid python datatypes 
# tuple unpacking
a,b,c,d = tuple1
print(a)
print(b)
print(c)
print(d)
# creating tuple with one element
tuple_solo = ("solo",)
print(type(tuple_solo)) #outputs typle
tuple_solo1 = ("solo")
print(type(tuple_solo1)) #outputs string
# accessing elements same as lists
print(tuple1[3])

# tuples can be reassigned
tuple_solo = (1,2,3,4)
print(tuple_solo)