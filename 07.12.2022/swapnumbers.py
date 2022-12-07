a=5
b=7 

def swapnum():
    global a
    global b
    temp = a
    a = b
    b = temp

print("before swapping",a,b)
swapnum()
print("after swapping",a,b)
