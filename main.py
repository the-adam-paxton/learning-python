from datetime import datetime
from datetime import date

print(datetime.today())
print(datetime.now())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().time())


now = datetime.now()
print(datetime.now())

print(now.strftime("%d-%m-%Y %H:%M:%S"))
print(now.strftime("%d-%B-%Y %H:%M:%S"))
print(now.strftime("%d-%b-%Y %H:%M:%S"))

print(date.today().strftime("%d-%m-%Y"))
