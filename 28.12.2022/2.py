def encryptmsg(msg):
    str2 = ''
    for i in msg:
        i = chr(ord(i)+3)
        str2 = str2+i
    return str2

print(encryptmsg('abcdef'))

