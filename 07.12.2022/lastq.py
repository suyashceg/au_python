def reqargs(a,b,c,d):
    return a+b+c+d

def keywordargs(a,b,c,d):
    return a++b+c+d

def defaultargs(a,b,c=5,d=4):
    return a+b+c+d

def variablelengthargs(a,*b):
    s = 0
    for i in b:
        s = s+i
    s+a
    return s


print("req args",reqargs(4,5,6,8))
print("keyword args",keywordargs(d=4,b=6,c=9,a=1))
print("default args",defaultargs(6,7))
print("variablelength args",variablelengthargs(1,2,3,4,5,6,7,8,9,10))
