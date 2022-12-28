def centrealign(num):
    space = 10-len(str(num))
    halfspace = int(space/2)
    for i in range(halfspace):
        print(" ",end='')
    print(num)
    for i in range(halfspace):
        print(" ",end='')


centrealign(int(input()))
