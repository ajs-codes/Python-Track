# declaration
from typing import Sequence

# declaration
# used to iterate string
sequence = 'string'
for num in sequence:
    print(num)
# used to iterate specified nums of time
for num in range(101):
    print(num)
print('numbers printed 0 to 100')
# example 2
for num in range(1, 101):
    print(num,end=' ')
print('\n')
# iterating through a list and tuple
list1 = ['a','b','c','d','e']
for item in list1:
    print(item)

sequence1 = (2,4,6,'11','8')
for item1 in sequence1:
    print(item1)
print('iterated through a tuple')

# method 2
names = ['sharan','karthic','ravi']

for name in range(len(names)):
    count = name+1
    print(f'{count} : {names[name]}')
print('iterated the names of list and outputting with key')

# for with else part
for name in names:
    print(name)
else:
    print('no items left')

