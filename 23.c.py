units = int(input("enter the no of units consumed"))
total = 0
if(units<151):
    total = units*3
elif(units>150 and units<351):
    total = 150*3 + 3.75*(units-150) + 100
elif(units>350 and units<451):
    total = 150*3 + 200*3.75 + 100 + (units-350)*4 + 250
elif(units>450 and units<601):
    total = 150*3 + 200*.375 + 100 + 100*4 + 250 + (units-450)*4.25 + 300
else:
    total = 150*3 + 200*.375 + 100 + 100*4 + 250 + 150*4.25 + 300 + (units-600)*6 + 400
print(total)    
