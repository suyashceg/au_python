file1 = open('abc.txt',mode='r+')
file2 = open('def.txt','r+')
content1 = file1.read()
content2 = file2.read()
file1.seek(0)
file2.seek(0)
file1.write(content2)
file2.write(content1)
file1.close()
file2.close()
