from datetime import datetime
from dateutil import relativedelta
from datetime import datetime

current_date = input("enter today's date")
dob = input("enter your birth date")
t1 = datetime.strptime(current_date, "%d/%m/%Y")
t2 = datetime.strptime(dob, "%d/%m/%Y")
delta = t1-t2
diff = relativedelta.relativedelta(t1, t2)
print(diff.years)
