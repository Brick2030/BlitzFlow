import os
import pickle
import time
import widgets
import datetime
from prettytable import PrettyTable
import random
import settings
import math
import weekcalculator

status_msg = "Welcome to the BlitzFlow..."


# Naming files for saving.
current_date = datetime.date.today()
#year = current_date.strftime("%Y")
#month = current_date.strftime("%m")
day = current_date.strftime("%d")
DateName: str = current_date.strftime("%Y/%m/")
#DateName: str = year + "/" + month + "/"
#TodayFileName = settings.SaveDirectory + current_date.strftime("%d-%m-%Y") + ".task"
#TodayFilePath = DateName
#TodayFilePath = settings.SaveDirectory + DateName

TodayFileName = DateName + day + ".task"



class TaskClass:
    def __init__(self, cycles, name, result):
        self.cycles = cycles
        self.name = name
        self.result = result 


# Different type of lists. Helps managing different kind of tasks after saving file.
UnfinishedLIST = []
FinishedLIST = []
FailedLIST = []
GlobalLIST = [UnfinishedLIST, FinishedLIST, FailedLIST] # ARRAY OF ARRAYS. ONGOING, FINISHED, FAILED
rand10_array = [] # random 10 NUMBERS OF GOALS from goal array.
RandGoalsArray = [] # Random goals from goal array.

# Bools for output management
ShowUnfinished = True
ShowFinished = True
ShowFailed = True


class Goal: # Class from goalmanager. Here until I figure it out how to combine those 2 apps into 1.
    def __init__(self, name, status):
        self.status = status
        self.name = name

##############################[Controls]#################################################
def saveas(day: str, month: str, year: str):
    namepath = (f"/{year}/{month}/")

    os.makedirs(os.path.dirname(settings.SaveDirectory + namepath), exist_ok=True)
    with open(settings.SaveDirectory + namepath + day + ".task", "wb") as f:
        pickle.dump(GlobalLIST, f)
    

def returnCycles():
    Time = time.localtime()
    hour = Time.tm_hour + Time.tm_min/60
    delta = (settings.sleepTime - hour) / settings.cycleTime
    return ("%.0f" % (round(delta)))

def save(): # goals are array
    os.makedirs(os.path.dirname(settings.SaveDirectory + DateName), exist_ok=True)
    with open(settings.SaveDirectory + TodayFileName, "wb") as f:
        pickle.dump(GlobalLIST, f)

def load(filename):
    with open(filename, "rb") as f:
        loaded_goals = pickle.load(f)
    return loaded_goals # return array

def showList(arrayName):
    TaskTab = PrettyTable()
    TaskTab.clear()
    TaskTab = PrettyTable(['Index','Cycles', 'Name', 'Result'])
    TaskTab.align = "r"
    cyclesSumm = 0
    resultSumm = 0

    for x, i in enumerate(arrayName):
        TaskTab.add_row([x, i.cycles, i.name, i.result])
        cyclesSumm = cyclesSumm + int(i.cycles)
        resultSumm = resultSumm + int(i.result)

    print(TaskTab)
    # Kinda weird system, it mostly useful for planning the start of the day, but when a lot of tasks
    # already completed it's almost not usable at all. 
    # Problem in the tab system itself, it must be changed.
    print(f"Cycle summ is {cyclesSumm} / {settings.MaxCycle} ({cyclesSumm/settings.MaxCycle*100}%)| Result summ is {resultSumm} / {settings.MaxCycle} ({resultSumm/settings.MaxCycle*100}%)\n")

def add(cycles, name):
    add_task = TaskClass(cycles, name, "0")
    UnfinishedLIST.append(add_task)

def fail(index):
    temp_task = UnfinishedLIST[index]
    FailedLIST.append(temp_task)
    UnfinishedLIST.pop(index)

def finish(index, cycles):
    temp_task = UnfinishedLIST[index]
    temp_task.result = cycles
    FinishedLIST.append(temp_task)
    UnfinishedLIST.pop(index)

def ShowStatus(msg):
    global status_msg
    status_msg = "Status: " + msg



##############################[Main Core]#################################################
quote = widgets.info() # Object for quote.

while(True):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(quote.rand_quote()) # Random Quote.
    
    print(f"Week number is {weekcalculator.NumberOfWeek()} / 52 ({str(weekcalculator.NumberOfWeek()/52*100)[0:5]}%)\n")
    
    day_of_month = datetime.date.today().day
    # Im lazy to get max num of every month. So I just use 30.
    print(f"Today is {day_of_month} day. (Month is {round(day_of_month/30*100, 2)}% over...)")

    day_of_week = datetime.date.today().weekday() + 1
    print(f"Day of week {day_of_week} (Week is {round(day_of_week/7*100, 2)}% over...)\n")
        
    # Wake up is at 9 am. Hardcoded yet. Later must be choosed in settings.
    print(f"Cycles until sleep: {returnCycles()} / 30 (Day is {round(100.0-int(returnCycles())/30*100, 2)}% over...) \n", "= = = "*5)

    if(ShowUnfinished):
        print("ONGOING")
        showList(UnfinishedLIST)
    if(ShowFinished):
        print("FINISHED")
        showList(FinishedLIST)
    if(ShowFailed):
        print("FAILED")
        showList(FailedLIST)

    # Status window for showing messages to user;
    print("- - - " * 15, "\n")
    print(status_msg)


##############################[Commands]########(Included in while)#######################

    com = input() # Command input
    
    match com:

        case "saveas": # Editing old or future files.
            day = input("Enter day: ")
            month = input("Enter month: ")
            year = input ("Enter year: ")
            saveas(day, month, year)
            ShowStatus(f"Saved as {year}/{month}/{day}.task.")

        case "save":
            save()
            ShowStatus("Saved for today's date file")

        case "load":
            #inp = input("Enter file name: dd-mm-yy without .task extension: ")
            inp = input("Enter year\month\day without .task extension: ")

            if (len(inp) == 0): inp = TodayFileName[0:len(TodayFileName)-5] # If nothing typed, loads today's note.
            #GlobalLIST = load(inp)
            GlobalLIST = load(settings.SaveDirectory + inp + ".task")

            UnfinishedLIST = GlobalLIST[0]
            FinishedLIST = GlobalLIST[1]
            FailedLIST = GlobalLIST[2]
            # What is this line? 
            #GlobalLIST = [UnfinishedLIST, FinishedLIST, FailedLIST] # ARRAY OF ARRAYS. ONGOING, FINISHED, FAILED
            ShowStatus("Loaded")

        case "add":
            temp_c = input("Cycles to finish: ")
            temp_n = input("Task name:")
            add(temp_c, temp_n)
            ShowStatus(f"Added {temp_n}")

        case "fail":
            temp_index = input("Index to fail: ")
            fail(int(temp_index))
            ShowStatus("Task failed")

        case "finish":
            temp_index = input("Index to finish: ")
            temp_efficiency = input("Cycles used: ")
            finish(int(temp_index), int(temp_efficiency))
            ShowStatus("Task finished")

        case "remove":
            temp_index = input("Index to remove: ")
            ShowStatus(f"Removed {UnfinishedLIST[int(temp_index)].name}...")
            UnfinishedLIST.pop(int(temp_index))

        case "less":
            ShowFailed = False
            ShowFinished = False
            ShowStatus("Less mode enabled")

        case "more":
            ShowFailed = True
            ShowFinished = True
            ShowStatus("Less mode disabled")

        case "help":
            ShowStatus("more, less, remove, finish, fail, add, load, save, saveas")

        case "exit":
            quit()



