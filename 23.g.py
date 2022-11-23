import math

def makepattern(a):
    while(a>0):
        count=10
        count2=2
        tempa = a
        temp = tempa%10000
        print("{}            {}".format(a,temp))
        a = a//10
        count=math.pow(count,count2)
        count2 = count2+1

a =int(input("enter any 5 digit number"))
b = (len(str(a)))
if(b!=5):
    print("invalid input")
else:
    makepattern(a)
