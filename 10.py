def palin(msg):
    msg2=msg[::-1]
    if msg==(msg2):
        return True
    else:
        return False


print(palin("anna"))
