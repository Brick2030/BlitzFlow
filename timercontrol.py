import os
import pickle
import time
import tasks
import widgets
import cycles
import datetime


# Обновить ввод циттат. Разнообразить их.
# Попробывать форматировать вывод в таблицу. Посмотреть библиотеки.
# Сделать возможность сохранения рабочей сессии как в goalmanager

# Таблица теперь объект. она содержит другие объекты. Поле таблицы это объект задача и индекс 
#в массиве этой задачи. (использовать ли словарь?). Всякие поля в таблице (названия, статистика, 
# сумма) теперь являются частью таблицы такой же, как и объекты. Научится считывать ширину окна и 
# подгонять таблицу под ширину. Таблицы должны создаваться минимальным набором комманд.

# Таблица как объект будет сохраняться загружаться удаляться, отобраться и т.д.


taskList = []

def add(ccycles, name, status, result):
    task1 = tasks.task(ccycles, name, status, result)
    taskList.append(task1)

def remove(index):
    taskList.pop(index)

def complete(index, time):
    taskList[index].ChangeStatus(3)
    taskList[index].ChangeResult(time)

def fail(index):
    taskList[index].ChangeStatus(0)

def move(index, index2):
    tempObj = taskList[index2]
    taskList[index2] = taskList[index]
    taskList[index] = tempObj

# Naming files for saving.
current_date = datetime.date.today()
TodayFileName = current_date.strftime("%d-%m-%Y") + ".task  "
#print(TodayFileName)


def save(): # goals are array
    with open(TodayFileName, "wb") as f:
        pickle.dump(taskList, f)

def load(filename):
    with open(filename, "rb") as f:
        loaded_goals = pickle.load(f)
    return loaded_goals # return array


quote = widgets.info() # Object for quote.


# Раздробить цельный список обхектов в несколько списков по статусам.






while(True):
    os.system('cls' if os.name == 'nt' else 'clear')

    print(quote.rand_quote()) # Random Quote.

    print("Cycles until sleep:", cycles.returnCycles(), "\n")
    print("%7s %10s %40s %10s %10s %20s" % ("[Index]", "[Cycles]", "[Name]", "[Status]", "[Result]", "[Result 2]")) # Header format.


    cycleSumm = 0 # Summ of cycles.
    for x, i in enumerate(taskList): # This loop outputs tasks that need to be solved rn.
        array = i.ReturnTask() # Array = one task. It's array bc it returns array.


        if (array[2] == "Nothing" or array[2] == "Ongoing"):
            cycleSumm = cycleSumm + int(array[0])
            print("%7s %10s %40s %10s %10s %20s" % (str(x), str(array[0]), array[1], array[2], str(array[3]), "NO RESULT"))
   
    print("%10s" % ("Summ: "), cycleSumm)

    
    for x, i in enumerate(taskList): # Second table for completed tasks
        array = i.ReturnTask() # array = task. 
        if(array[2] == "Completed"):
            print("%7s %10s %40s %10s %10s %20s" % (str(x), str(array[0]), array[1], array[2], str(array[3]), str(float(array[3])/float(array[0])*100)), "%")


    com = input() # Command input
    
    match com:
        case "add":
            TaskCycles = input("cycles: ")
            TaskName = input("name: ")
            add(TaskCycles, TaskName, 1, 0)

        case "finish":
            index = input("Index to complete: ")
            time = input("How many cycles used to finish: ")
            complete(int(index), (time))

        case "fail":
            index = input("Index to fail: ")
            fail(int(index))

        case "remove":
            index = input("Index to remove")
            remove(int(index))

        case "exit":
            quit()

        case "move":
            index = input("Enter index of task to move")
            index2 = input("Enter index where to move")
            move(int(index), int(index2))

        case "show delayed":
            print("Delayed tasks")
            # Сделать булеан переменную на отображения виджета отложенной задачи.
            # Стоит ли делать отложенную задачу подклассом обычной задачи?

        case "save":
            save()
            time.sleep(5)

        case "load":
            inp = input("Enter file name: dd-mm-yy without .task extension: ")
            taskList = load(inp + ".task")
            


        case "help":
            print("\nadd\nfinish\nfail\nremove\nhelp\nexit\nmove\n")
            i = input("type anything to close help: ")
