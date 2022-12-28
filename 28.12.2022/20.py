def f2l2(str1):
    mylist = []
    mylist.append(str1[0:2])
    mylist.append(str1[-2:])
  
    return ''.join(map(str,mylist))

print(f2l2("hello world"))
