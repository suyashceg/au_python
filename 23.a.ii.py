import math
x = int(input("enter any number"))
y = int(input("enter the no upto which you want the series"))
sum = 0
for i in range(1,y+1):
    sum = sum + math.pow(-x,i)
print(sum)
