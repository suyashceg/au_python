def fun1(str1):
    str2 = str1[0].upper()+str1[1:]
    return str2

def fun2(str1):
    mylist = str1.split()
    str2 = mylist[0][0].upper()+mylist[0][1:]+" "+mylist[1][0].upper()+mylist[1][1:]
    return str2

def fun3(str1):
    mylist=[]
    for i in str1:
        mylist.append(i.swapcase())
    return ''.join(map(str,mylist))

def fun4(str1):
    str2 = str1[0].upper()+str1[1:]
    return str2.replace('world','Friends')

print(fun1("hello world"))  
print(fun2("hello world"))
print(fun3("hello WORLD"))
print(fun4("hello world"))
