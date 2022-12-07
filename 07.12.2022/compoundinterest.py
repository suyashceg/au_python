def compoundinterest(p,r,t):
    amount = p * (pow((1+r/100),t))
    ci = amount - p
    return ci

print(compoundinterest(1000,5,3))
