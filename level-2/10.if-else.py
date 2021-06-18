# declation
int1 = int(input('enter a number: '))

if int1 > 0:
    print(f'{int1} is positive number')
else:
    print('zero or negative')

# multiple if-else statements
if int1 > 5:
    print('this goes for A')
elif int1 == 5:
    print(f'this is {int1}')
elif int1 < 5 and int1 >= 1:
    print(f'its a foul')
else:
    print('zero or negative')

# nested 
if int1 >= 0:
    if int1 == 0:
        print('this number is zero')
    else:
        print('this number is positive')
else :
    print('this number is negative')
print("this is nested if-else statement")


