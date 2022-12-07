def f(x,y):
    if y<=x:
        x = (x-y)
        y+=1
    return x,y

x,y = f(5,4)
print(x,y)
