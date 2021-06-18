# understanding break and continue statements

a = input('enter a string : ')
# print upto str
for i in a:
    if i == ' ':
        break # this breaks the loop and jump out
    print(i,end='')
print()
# continue
# omitting i and g
for i in a:
    if i == ' ':
        continue
    print(i, end='')
# pass statement
# this should be declared when a statement is empty
# for example

for i in a:
    pass
while True:
    pass
def func():
    pass
class Table:
    pass


