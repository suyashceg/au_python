def checkletter(msg,letter):
    count=0
    for i in msg:
        if(i==letter):
            return count
        count+=1
    return -1

str1 = input("enter the string")
l = input("enter a letter")
n = checkletter(str1,l)
if(n==-1):
    print("letter not present")
else:
    print("letter is at position",n)
        
        
