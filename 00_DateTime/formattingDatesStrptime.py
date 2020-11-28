from datetime import datetime
date_string = "28 October, 2020"

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("The date object is: ", date_object)

print('-------Seperator Line-------')

dateOne = "12/10/2020 07:43:22"
date_objectOne = datetime.strptime(dateOne, "%d/%m/%Y %H:%M:%S")
print("date_objectOne: ", date_objectOne)
#considering it to be in month and date and year format.
date_objectTwo = datetime.strptime(dateOne, "%m/%d/%Y %H:%M:%S")
print("date_objectTwo", date_objectTwo)

timestamp = datetime.timestamp(date_objectTwo)

#converting the date object to Unix Timestamp.

timestamp = datetime.timestamp(date_objectTwo)
print("The unix Timestamp is ", timestamp)
'''
Converting it back to datetime.
'''
date_time = datetime.fromtimestamp(timestamp)
d = date_time.strftime("%c")
print("Output 1:", d)
d = date_time.strftime("%x")
print("Output 2:", d)
d = date_time.strftime("%X")
print("Output 3:", d)

