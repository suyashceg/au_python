#Write a program to prepare a grocery bill, enter the name of the items purchased, quantity in which it is purchased, and its price per unit.Display the bill in the following format.

n = int(input("how many products you want to enter"))
product = [0 for i in range(0,n)]
quantity = [0 for i in range(0,n)]
price = [0 for i in range(0,n)]
total = 0
for i in range(0,n):
    product[i] = input("enter name of the product")
    quantity[i] = int(input("enter the quanitity of the product"))
    price[i] = int(input("enter the price pf the product"))

print("***************************BILL*************************")
print("{}   {}    {}".format("name","quantity","price"))
for i in range(0,n):
    print("{}        {}        {}".format(product[i],quantity[i],price[i]*quantity[i]))
    total = total + price[i]*quantity[i]

print("*********************************************************")
print("Total Amount to be paid",total)
print("*********************************************************")

    


