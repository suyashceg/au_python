#Write a python program to calculate simple interest and compound interest.

p = float(input("enter principal amount"))
r = float(input("enter the rate of interest"))
t = float(input("enter time period"))
si = (p*r*t)/100
ci = p*(pow((1+r/100),t)) - p
print(si)
print(ci)
