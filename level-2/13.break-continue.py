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



