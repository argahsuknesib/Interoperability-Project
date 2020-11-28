from datetime import datetime, time

timestamp = 1603444784.251691

dt_object = datetime.fromtimestamp(timestamp)

print("DateTime Object --> ", dt_object)
print("The type of DateTime Object will be --> ", type(dt_object))

"""
Output :

DateTime Object -->  2020-10-23 11:19:44.251691
The type of DateTime Object will be -->  <class 'datetime.datetime'>

"""