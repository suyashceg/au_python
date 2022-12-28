def isX (name,pan):
    if (name.isalpha() == 0) or (pan.isalnum() == 0):
        print("enter valid characters")
        return
    else:
        print("name: ",name,"pan: ",pan)

name = input('enter your name')
pan = input("enter your pan number")
isX(name,pan)
