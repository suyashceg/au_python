hourlywage = int(input("enter hourly wage"))
hours = int(input("no of hours"))
overtime = int(input("no of overtime hours"))

print("wage: "+str(hourlywage*hours+overtime*hourlywage*1.5))
