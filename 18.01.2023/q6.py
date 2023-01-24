file1 = open('abc.txt','r')
content = file1.read()
newcontent = ''
flag = False
for i in content:
    if i == '.':
        flag=True
        newcontent+=i
        continue
    if flag is True:
        if ord(i)>=48 and ord(i)<=57:
            newcontent = newcontent+"["+i+"]"
        else:
            newcontent+=i.upper()
    else:
        newcontent+=i
print(newcontent)