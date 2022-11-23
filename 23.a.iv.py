import math

x = int(input("enter the value of x"))
y = int(input("enter the no upto which you want the series"))
total = 0
for i in range(0,x+1):
    total = total + math.pow(-1,i)*math.pow(x,i)/math.factorial(i)

print(total)
