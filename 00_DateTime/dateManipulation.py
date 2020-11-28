from datetime import date, datetime, timedelta

now = datetime.now()
print("Today's Date --> ", str(now))

date_15_days_from_now = now + timedelta(days = 15)
print('The date after 15 days will be, ', date_15_days_from_now)

two_weeks_ago = now - timedelta(weeks=2)
print('Two weeks ago, the date was', two_weeks_ago)
print('two_weeks_ago object type is ', type(two_weeks_ago))

