import cycles

CyclesLeft = cycles.returnCycles()



class Timer():

    def ShowCycles(self):
        print ("Cycles until sleep time: ", CyclesLeft)

    def AddTask(self, plan, name):
        print("Task added")
