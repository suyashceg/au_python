file1 = open('abc.txt')
mystr = file1.read()
mystr2 = mystr[::-1]
print(mystr2)
file1.close()

file2 = open('def.txt',mode='w')
file2.write(mystr2)
file2.close()
