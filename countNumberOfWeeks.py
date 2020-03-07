import datetime
from datetime import date, timedelta

# Goal is to create a script that counts the total number of weeks that passed in the past 90 days
# Define a week as the iso week number

# find the time right now.
now = datetime.datetime.now()

print("Today is ... " + str(now))

# find the day 90 days ago from today
date_90_days_ago = now - timedelta(days=90)

print("90 days ago was ... " + str(date_90_days_ago))

# Use isocalendar to extract details about time
# isocalendar() returns a 3-tuple, (ISO year, ISO week number, ISO weekday).
date_90_days_ago_ISO = date_90_days_ago.isocalendar()
now_ISO = now.isocalendar()

# subtract week number of 90 days ago with week number of today
weeks = date_90_days_ago_ISO[1] - now_ISO[1]
#print(weeks)

# Heres the final answer...
print("There were " + str(weeks) + " weeks in the past 90 days.")