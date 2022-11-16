#Write a program that reads the address of a user. Display the result bybreaking it in multiple lines.
print(r"write your address and enter . to change line of address")
address = input()
n = address.split('.')
for i in n:
    print(i)
