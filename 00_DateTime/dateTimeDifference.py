from datetime import date
from datetime import datetime
date1 = date(2016, 8, 21)
date2 = date(2018, 8, 11)

delta = date2 - date1
print("The difference between the dates is ", delta.days)
print("The object type is ", type(delta))

'''
We can also describe the dates and time with
year, month, day, time, hour, seconds.
You can see the code below.
'''
print("----------Seperator Line----------\n")

dateOne = datetime(2018, 6,23,18,23,45)
dateTwo = datetime(2020, 11, 12, 20, 6, 43)

diff = dateTwo - dateOne
print("The difference is: ", diff)
