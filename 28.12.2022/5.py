def redefined(msg):
    vowel = ('a','e','i','o','u')
    lst = []
    for i in msg:
        if i in vowel:
            pass
        else:
            lst.append(i)
    return lst

lst = redefined("abcedfg")
lstr = ''.join(map(str,lst))
print(lstr)
