# *args arguments can take n no of arguments make it as tuple
# for example
def greet_groups(*names):
    print(type(names))
    for i in names:
        print(F'hey {i}')

greet_groups('sharan','sairam','karthic','ravi','hello world')
# another example
def add_list(*no):
    if no == ():
        return "None"    
    else:
        sum = 0
        for i in no:
            sum += i 
        return sum 

print(add_list(1,2))

# **kargs arguments can take n no of keyword arguments and make it as dicts
# for example
def forms(**kform):
    for key,value in kform.items():
        print(f'{key} = {value}')

    
forms(name = 'ajs',age = 20,homeplace = 'coimbatore')


