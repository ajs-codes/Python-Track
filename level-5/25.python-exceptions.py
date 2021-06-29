# exceptional handling are used when error occurs
# used for run-time errors
# to resolve error we write exception blocks like try,catch,finally
x = ''
y = ''
try:
    z = x/y
    print(z)
except:
    print("error!, you can't divide a string")
# try statement look for error
# if error exist the code jumps to except block
# another example
try:
    num = int(input("enter a num: "))
    print(num)
except:
    print("error occured")

# multiple error handling based on the type of error
try:
    l = [2,3,4,6,8]
    i = int(input("enter the index: "))
    print(l[i])
except ValueError:
    print("invalid input")
except IndexError:
    print("given index is invalid")
except:
    print("unknown error occured")
# finally block (this block always executes)
finally:
    print("program ends")

