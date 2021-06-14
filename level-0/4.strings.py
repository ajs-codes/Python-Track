# here we will going to see about,
# string declaration,formatting and methods

# declaration
str1 = "hello world! \n"
str2 = "this is sharan's laptop. \n"
str3 = 'this is a "quotation". \n'
str4 = '''
hello world 
my name is sharan
my age is 20
i am a passionate boy who 
loves and learn to coding.
'''
print(str1+str2+str3)
print(str4)

# accessing chars in a string
index = "python"
print(index[0],',',index[3],',',index[-1])
group_str = "hello world"
print(group_str[0:7],',',group_str[1:],',',group_str[:-2],',',group_str[:])

# formatting strings
first_name = "Sharan"
last_name = "AJ"
message = f"hey, {first_name} {last_name}"
print("\n"+message)

# few examples of string methods
name = "sHAran"
# to find in length
print(len(name))
# to captalize
print(name.capitalize())
# to upper
print(name.upper())
# to lower
print(name.lower())
# to find the index
print(name.find('h'))
# to replace
print(name.replace('n','n AJ'))
# the in keyword
print("AJ" in name)