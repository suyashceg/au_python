import math

n = int(input("enter the number of terms"))
for i in range(1,n+1):
    print(int(math.pow(i,3)),end="   ")


print()

for i in range(1,n+1):
    print((-2)*i,end="   ")

print()

for i in range(0,n):
    print(1+3*i,end="   ")
    

    
