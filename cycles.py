#from time import ctime
import time
import math

def returnCycles():
    sleepTime = 24 # Move to settings file
    cycleTime = 0.5

    Time = time.localtime()
    hour = round(Time.tm_hour + Time.tm_min/60)

    delta = (sleepTime - hour) / cycleTime

    return int(delta)
