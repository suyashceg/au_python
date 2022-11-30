str = input("enter any number")
strlen = len(str)
j=1
for i in range(0,len(str)):
    print(" "*i,end="")
    print(str[i:],end="")
    print(" "*5,end="")
    print(str[:j])
    j+=1
    

