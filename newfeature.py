import settings
from datetime import datetime
import math

def NumberOfWeek():
    Month = settings.YearStartMonth

    some_date = datetime(2022, Month, 1)
    now_date = datetime(2023, 9, 1)
    
    #now_date = datetime.now()
    delta = (now_date - some_date).days+1
    delta2 = (now_date - testdate).days+1
    print("delta2", delta2)
    year_delta = (now_date.year - some_date.year)
    print("year delta", year_delta)

    firstday = some_date.isocalendar().weekday
    weeknum = 1

    for i in range(delta):
        DAY = firstday + i
        if DAY > 7:
            DAY = 1
            weeknum = weeknum + 1
            firstday = firstday - 7
            
    return(weeknum)




print(NumberOfWeek())

