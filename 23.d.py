from datetime import datetime

vehicle = input("what type of vechicle")
str1 = (input("enter entry time"))
str2 = (input("enter exit time"))
start_time = datetime.strptime(str1, "%H:%M:%S")
end_time = datetime.strptime(str2, "%H:%M:%S")
delta = end_time - start_time
sec = delta.total_seconds()
min = sec / 60
hrs = sec / (60 * 60)
total = 0
if(vehicle == "car"):
    if(hrs<=3):
        total = hrs*10
    else:
        total = 30+20*(hrs-3)
elif(vehicle == "truck" or vehicle == "bus"):
    if(hrs<=3):
        total = hrs*20
    else:
        total = (hrs-3)*30+60
elif(vehicle == "cycle" or vehicle == "motorcycle" or vehicle == "scooter"):
    if(hrs<=3):
        total = hrs*5
    else:
        total = 15+(hrs-3)*10
print(total)
