# list declaration
list1 = [1,2,3,4,5]
list2 = ['hello','hey','what\'s up','buddy']
# mutable and allows duplicate
# accessing items
print(list1)
print(list2)
print(list1[4])
print(list2[3])
print(list1[-1])
print(list2[-2],list2[-1])
print(list1[0:-1])
print(list2[:-2])

# modifing items
list1[-1] = 10
list2[0:2] = ['sharan','karthic']
print(list1)
print(list2)
list2[:] = ['ajs']
print(list2)

# inserting items
list2.insert(1,'karthic')
list2.insert(2,'ravi kumar')
print(list2)

# adding to the end of the list (append)
list2.append('sudharsan')
print(list2)

# extending the list
list3 = ['sairam','durai','bms']
list2.extend(list3)
print(list2)

# removing items in a list
list3.remove('bms')
print(list3)
list2.pop()
print(list2)
list2.pop(3)
print(list2)

# for deleting the list
del list3
# for clearing the list
list1.clear()
print(list1)
del list1

# other list methods
list2.reverse()
print(list2)
list2.sort()
print(list2)


