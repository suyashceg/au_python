def divbym(m,n):
    if(m>=n):
        return
    else:
        for i in range(1,n+1):
            if(i%m==0):
                print(i)


divbym(10,100)
