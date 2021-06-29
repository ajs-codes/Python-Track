# program to cover the topics of file handling
# open,create,read and write,close operations

# opening a file
# file1 = open('message.txt','r') #read mode only
# file2 = open('message.txt','w') #write mode only
# file3 = open('message.txt','r+') #read and write mode
# file4 = open('message.txt','a') #append mode

# reading the file
f = open('message.txt','r')
content = f.read()
print(content, type(content))
f.close() #function to close a file

# more about read function
f1 = open('message.txt','r')
content1 = f1.read(10)
print(content1)
f1.close()

# readline
content2 = []
f2 = open('message.txt','r')
content2.append(f2.readline())
content2.append(f2.readline())
print(content2)
print(content2[0],content2[1],sep='')
f2.close()

# readlines
f3 = open('message.txt', 'r')
lines = f3.readlines()
print(lines)

# writing to the file and reading it
f4 = open('msg.txt','w')
f4.write(f'hello msg.txt, i am sharan!\n')
f4.close()

# appending to file
f5 = open('msg.txt', 'a')
f5.write('this is a new line')

# writelines
f6 = open('msg2.txt', 'w')
msgs = ['sharan','aj\n','20 years old\n','pursuing bca final year']
f6.writelines(msgs)
