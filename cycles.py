#from time import ctime
import time
import math
import settings

def returnCycles():

    Time = time.localtime()
    hour = Time.tm_hour + Time.tm_min/60
    delta = (settings.sleepTime - hour) / settings.cycleTime

    return ("%.0f" % (round(delta)))

