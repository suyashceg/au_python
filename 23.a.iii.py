x = int(input("enter the no upto which you want the series"))
total = 0
for i in range(1,x+1):
    total = total + sum(range(1,i+1))
print(total)
