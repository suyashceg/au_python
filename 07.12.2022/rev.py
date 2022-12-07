def reverse(n):
    if n<10:
        print(n)
        return
    else:
        print(n%10,end="")
        reverse(n//10)

reverse(1234)
