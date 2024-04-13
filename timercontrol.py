import os
import pickle
import time
import widgets
import cycles
import datetime
from prettytable import PrettyTable

# TODO
# Обновить ввод циттат. Разнообразить их.
# Попробывать форматировать вывод в таблицу. Посмотреть библиотеки.
# Сделать возможность сохранения рабочей сессии как в goalmanager
# Раздробить цельный список обхектов в несколько списков по статусам.



# FINISHED
# Таблица теперь объект. она содержит другие объекты. Поле таблицы это объект задача и индекс 
#в массиве этой задачи. (использовать ли словарь?). Всякие поля в таблице (названия, статистика, 
# сумма) теперь являются частью таблицы такой же, как и объекты. Научится считывать ширину окна и 
# подгонять таблицу под ширину. Таблицы должны создаваться минимальным набором комманд.
# Таблица как объект будет сохраняться загружаться удаляться, отобраться и т.д.



# Naming files for saving.
current_date = datetime.date.today()
TodayFileName = current_date.strftime("%d-%m-%Y") + ".task"

# Main Class for task object
# 0 - Ongoing.
# 1 - Finished
# -1 - Failed (delayed).
# Object will store only number status. And table itself will translate it words
# Or maybe it's better to use dictionary. But why to complicate such simple things.
class TaskClass:
    def __init__(self, cycles, name, status, result):
        self.cycles = cycles
        self.name = name
        self.result = result 


# Different type of lists. Helps managing different kind of tasks after saving file.
UnfinishedLIST = []
FinishedLIST = []
FailedLIST = []
GlobalLIST = [UnfinishedLIST, FinishedLIST, FailedLIST] # ARRAY OF ARRAYS. ONGOING, FINISHED, FAILED


#taskList = [] # MAIN ARRAY OF TASKS
quote = widgets.info() # Object for quote.

# Bools for output management
ShowUnfinished = True
ShowFinished = True
ShowFailed = True


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

    for x, i in enumerate(arrayName):
        TaskTab.add_row([x, i.cycles, i.name, i.result])
        cyclesSumm = cyclesSumm + int(i.cycles)

    print(TaskTab)
    print(f"Cycle summ is {cyclesSumm}\n")

def add(cycles, name):
    add_task = TaskClass(cycles, name, "0", "0")
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





##############################[Commands]########(Included in while)#######################

    com = input() # Command input
    
    match com:
        case "save":
            save()

        case "load":
            inp = input("Enter file name: dd-mm-yy without .task extension: ")
            #GlobalLIST = load(inp)
            GlobalLIST = load(inp + ".task")

            UnfinishedLIST = GlobalLIST[0]
            FinishedLIST = GlobalLIST[1]
            FailedLIST = GlobalLIST[2]
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



