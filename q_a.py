#Write a program to enter two integers and then perform all arithmetic operations on them

a = int(input("enter first number"))
b = int(input("enter second number"))

print("enter 1 to perform addition")
print("enter 2 to perform substraction")
print("enter 3 to perform multiplication")
print("enter 4 to perform division")

c = int(input())

if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)
else:
    print("wrong choice")
