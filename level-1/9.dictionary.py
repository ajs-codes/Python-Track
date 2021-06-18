# this data type as key : value pairs of data
my_dict = {}
my_dict = {'name1' : 'john','name2' : 'sharan','name3' : 'karthic'}
print(my_dict)
# can be entered any data type numbers,strings,boolean,list,tuples,set
# each data can be accessed using a key
print(my_dict.get('address'))
print(my_dict['name2']) 
# adding and updating elements
my_dict['name1'] = 'ravi'
print(my_dict)
my_dict['name4'] = 'sai ram'
print(my_dict)
# accessing keys
print(list(my_dict.keys()))

# removing items
my_dict.pop('name1')
print(my_dict)
my_dict.popitem() #removes last element
print(my_dict)
my_dict.clear()
print(my_dict)
del my_dict

