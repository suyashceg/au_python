file1 = open('abc.txt','r')
list1 = file1.readlines()
for i in list1:
    anotherlist = i.split()
    if 'print' in anotherlist:
        print(i,end='')
file1.close()