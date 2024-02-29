#from time import ctime
import time

def returnCycles():
    sleepTime = 24
    cycleTime = 0.5

    print("Hello world")


    Time = time.localtime()
    hour = float(Time.tm_hour + Time.tm_min/60)
    print(hour)

    delta = (sleepTime - hour) / cycleTime

    return delta
