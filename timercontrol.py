import os
import pickle
import time
import widgets
import cycles
import datetime
from prettytable import PrettyTable
import random
import settings




# Naming files for saving.
current_date = datetime.date.today()
TodayFileName = settings.SaveDirectory + current_date.strftime("%d-%m-%Y") + ".task"


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

#taskList = [] # MAIN ARRAY OF TASKS
quote = widgets.info() # Object for quote.

# Bools for output management
ShowUnfinished = True
ShowFinished = True
ShowFailed = True


class Goal: # Class from goalmanager. Here until I figure it out how to combine those 2 apps into 1.
    def __init__(self, name, status):
        self.status = status
        self.name = name


##############################[Controls]#################################################

def save(): # goals are array
    with open(TodayFileName, "wb") as f:
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
    print(f"Cycle summ is {cyclesSumm} | Result summ is {resultSumm}\n")

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

def randomGoals():
    with open(settings.SaveDirectory +settings.GoalManagerFileName, "rb") as f:
        loaded_goals = pickle.load(f)

    rand10_array.clear()
    RandGoalsArray.clear()
    for x in range(5):
        rand = random.randint(0, len(loaded_goals)-1)
        if (rand10_array.count(rand) > 0): continue
        rand10_array.append(rand)

    for x in rand10_array:
        RandGoalsArray.append([x, loaded_goals[x]])

    for goal in RandGoalsArray:
        print(goal[0], goal[1].name) 



##############################[Main Core]#################################################


while(True):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(quote.rand_quote()) # Random Quote.
    print("Cycles until sleep:", cycles.returnCycles(), "\n")
    
    if(ShowUnfinished):
        print("ONGOING")
        showList(UnfinishedLIST)
    if(ShowFinished):
        print("FINISHED")
        showList(FinishedLIST)
    if(ShowFailed):
        print("FAILED")
        showList(FailedLIST)

    randomGoals()



##############################[Commands]########(Included in while)#######################

    com = input() # Command input
    
    match com:
        case "save":
            save()

        case "load":
            inp = input("Enter file name: dd-mm-yy without .task extension: ")
            if (len(inp) == 0): inp = current_date.strftime("%d-%m-%Y") # If nothing typed, loads today's note.
            #GlobalLIST = load(inp)
            GlobalLIST = load(settings.SaveDirectory + inp + ".task")

            UnfinishedLIST = GlobalLIST[0]
            FinishedLIST = GlobalLIST[1]
            FailedLIST = GlobalLIST[2]
            # What is this line? 
            #GlobalLIST = [UnfinishedLIST, FinishedLIST, FailedLIST] # ARRAY OF ARRAYS. ONGOING, FINISHED, FAILED

        case "add":
            temp_c = input("Cycles to finish: ")
            temp_n = input("Task name:")
            add(temp_c, temp_n)

        case "fail":
            temp_index = input("Index to fail: ")
            fail(int(temp_index))

        case "finish":
            temp_index = input("Index to finish: ")
            temp_efficiency = input("Cycles used: ")

            finish(int(temp_index), int(temp_efficiency))

        case "remove":
            temp_index = input("Index to remove: ")
            UnfinishedLIST.pop(int(temp_index))
            
        case "less":
            ShowFailed = False
            ShowFinished = False

        case "more":
            ShowFailed = True
            ShowFinished = True

        case "exit":
            quit()



