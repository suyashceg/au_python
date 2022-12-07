recfn = lambda n : recfn(n//2)+1 if n>1 else 1

num = recfn(5)
print(num)
