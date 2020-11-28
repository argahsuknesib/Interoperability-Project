'''
pytz module helps us with dealing through
the cross-timezone conversions.
'''

from datetime import datetime
from pytz import timezone
east = timezone('US/Eastern')
loc_dt = east.localize(datetime(2011,11,2,7,27,0))
print(loc_dt)

kolkata = timezone("Asia/Kolkata")
print(loc_dt.astimezone(kolkata))

au_tz = timezone("Australia/Sydney")
print(loc_dt.astimezone(au_tz))
