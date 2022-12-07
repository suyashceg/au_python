def smdu(str):
    if str == 'S':
        return "separated"
    elif str == 'M':
        return "married"
    elif str == 'D':
        return "divorced"
    elif str == 'U':
        return "unmarried"
    else:
        return "invalid string passed"

print(smdu('S'))
