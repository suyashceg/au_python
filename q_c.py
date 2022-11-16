#Write a python program to perform string concatenation, Identify thevariant forms of python code to concatenate strings.

str1 = input("enter the first string")
str2 = input("enter the second string")

print("first method "+str1+str2)
print("second method "+"".join([str1, str2]))
print("third method "+"%s%s" % (str1, str2))
print("fourth method",str1,str2)
print("fifth method "+"{} {}".format(str1, str2))
