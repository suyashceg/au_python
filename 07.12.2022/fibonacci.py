def fibonacci(n):
    n1 = 1
    n2 = 1
    while(n>0):
        print(n1,end=" ")
        temp = n1
        n1 = n2
        n2 = n2+temp
        n-=1

def fibonacci_r(n):
    if n<=1:
        return n
    else:
        return(fibonacci_r(n-1) + fibonacci_r(n-2))

fibonacci(10)
print()

for i in range(1,11):
    print(fibonacci_r(i),end=" ")
