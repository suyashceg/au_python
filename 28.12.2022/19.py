def countstr(mystr):
    digits=0
    upcase = 0
    lcase = 0
    special = 0
    for i in mystr:
        if i.isnumeric():
            digits+=1
        elif i.isupper():
            upcase+=1
        elif i.islower():
            lcase+=1
        else:
            special+=1
    print("digits",digits)
    print("uppercase characters",upcase)
    print("lowercase characters",lcase)
    print("special characters",special)


str1 = input("enter a string")
countstr(str1)
    
        
