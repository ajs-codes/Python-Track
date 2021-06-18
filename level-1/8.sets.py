# creating a set
set1 = {1,2,3}
# set can have datatypes like numbers,string,tuple
# but it cannot have lists,sets and dicts
set_demo = {"hi","hello",(1,2,3),2.4,2,33}
print(set)
# set cannot have duplicates value
set2 = {1,1,4,6,3,2,4}
print(set2)
# it automatically removes the duplicate
# to initialize an empty set 
set3 = set()
print(type(set3))
set4 = {}
print(type(set4))
# modifing a set in python
# indexing and slicing will not work in sets
set_modify = set()
set_modify.add(5)
set_modify.add(3)
set_modify.update({3,6,8,77,100})
print(set_modify)

# removing elements from the set
# discard() and remove()
set_modify.remove(3)
print(set_modify)
set_modify.remove(5)
print(set_modify)
# set_modify.remove(5) #this throws an error
set_modify.discard(5) 
print(set_modify)

# also
set_demo.pop()
print(set_demo)
set_demo.clear()
print(set_demo)

# set operations
a = {'a','b','c','d','e',1,2,3}
b = {1,2,3,4,5,6,7,8,9,0}
# union operator |
print(a | b)
print(a.union(b))
print(b.union(a))
# intersection
print(a & b)
print(a.intersection(b))  #and vice versa
# difference
print(a - b)
print(b - a)
print(a.difference(b))
print(b.difference(a))
# set symmentric difference
print(a ^ b)
