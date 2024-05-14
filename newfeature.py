import settings
from datetime import datetime
import math

def NumberOfWeek():
    # Getting data from settings file.
    Month = settings.YearStartMonth
    YEAR = settings.YearStartYear
    # Testdate used for calculating year. I cant explain, but it's important.
    testdate = datetime(YEAR, Month, 1)
    # Today's date.
    now_date = datetime.now()

    # Delta between testdate and today. Used for calculating "true year" which is important
    delta2 = (now_date - testdate).days+1
    # Used for getting right date for week calculation.
    true_year = YEAR + (math.floor(delta2/365))
    # Start date for week calculation.
    some_date = datetime(true_year, Month, 1)
    # Delta used next for calculating week by each day.
    delta = (now_date - some_date).days+1 # Since it's gonna start with 0 it's important to +1
    # Firstday is weekday of some_date. Which is required for by-day calculation of week.
    firstday = some_date.isocalendar().weekday
    # Used for output. Will increase. 1 is default num.
    weeknum = 1

    for i in range(delta):
        DAY = firstday + i # DAY is weekday.
        if DAY > 7:
            DAY = 1 # if not do this, it will skip monday, and add "8th" weekday.
            weeknum = weeknum + 1 # Increasing output value.
            firstday = firstday - 7 # Drops to monday.
            
    return(weeknum) # Returns weekday.

# Expected problems: that year stuff. 
# I cant even explain or understand it. So probably it may be broken.
# So if any bugs will appear probably that's the reason.

#print("week num", NumberOfWeek())

