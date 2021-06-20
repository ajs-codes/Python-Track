# resursion is function calling itself like a loop 
# factorial example 
def fact(a):
    if a <= 1:
        return a
    else: 
        return (a * fact(a - 1))
    
no = int(input('enter a no to find its factorial: '))
print(fact(no))

# print the msg repeatedly using resursion
def greet_times(a,b):
    if b <= 0:
        return 0
    else:
        print(a)
        greet_times(a,b - 1)

msg = input("enter the msg to be repeated: ")
count = int(input('how many times to be repeated: '))
greet_times(msg,count)


# iterate a no using resursion
def iterate_nos(limit,count = 1):
    if count <= limit:
        print(count)
        iterate_nos(limit,count + 1)
        
no_of_times = int(input('enter the limit: '))
iterate_nos(no_of_times)