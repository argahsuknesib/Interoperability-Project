from datetime import datetime
date_string = "23 October 2020"
date_object = datetime.strptime(date_string, "%d %B %Y")
print("date_object:  ", date_object)

dt_string = "2/10/2020 12:05:12"
"""
as, we in this case don't know what format is the date is written in, we will try doing it with both formats.
It maybe a MM/DD format or a DD/MM format.

"""
#let's consider that it is a DD/MM format.
dt_object1 = datetime.strptime(dt_string, "%d/%m/%Y %H:%M:%S")
print("value of dt_object1 is ", dt_object1)

#let's consider that it is a MM/DD format.
dt_object2 = datetime.strptime(dt_string, "%m/%d/%Y %H:%M:%S")
print("value of dt_object2 is ", dt_object2)