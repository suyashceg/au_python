my_words = []
str = ""
for i in range(0,5):
    print("enter word")
    str = input()
    while(not(len(str)>=6)):
        print("enter word of atleast 6 characters")
        str = input()
    my_words.append(str)

for i in my_words:
              print(i)
