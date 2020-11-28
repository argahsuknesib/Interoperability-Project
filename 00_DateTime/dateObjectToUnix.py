from datetime import date, datetime

now = datetime.now()

timestamp = datetime.timestamp(now)

print("Date and Time : ", now)
print("Timestamp in UNIX : ", timestamp)

"""
Output for the program will be
Date and Time :  2020-10-23 11:19:44.251691
Timestamp in UNIX :  1603444784.251691
"""