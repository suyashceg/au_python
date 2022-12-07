def s_and_v(radius):
    s = 4*3.14*radius*radius
    v = 4/3*3.14*radius**3
    return s,v

s,v = s_and_v(50)
print(s,v)
