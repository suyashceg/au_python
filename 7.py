def countoccr(msg,letter):
    count=0
    for i in msg:
        if i==letter:
            count+=1
    return count

print(countoccr("abbccd","c"))
