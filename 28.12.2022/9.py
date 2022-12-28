def remodd(msg):
    mylst = []
    count=1
    for i in msg:
        if(count%2!=0):
            pass
        else:
            mylst.append(i)
        count+=1
    return ''.join(map(str,mylst))

print(remodd("hello world"))
