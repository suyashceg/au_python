#Write a python program to swap two numbers using a temporary variable.
a = 6
b = 7
print("before swapping "+"a: "+str(a)+" b: "+str(b))

temp = a
a = b
b = temp
print("after swapping "+"a: "+str(a)+" b: "+str(b))
