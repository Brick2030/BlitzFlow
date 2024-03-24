import pickle
import os
import settings
import random

# Добавить дату в объект Goal. ПРидумать как обновить существующие объекты под новый формат
# Придумать как объединить функционал goalmanager и timercontrol в одно приложение.
# Возможно стоит придумать еще пару приложений перед их совмещением
# Нужно придумать как объединить приложения. У них разное управление.
# Возможно стоит создать на основе этих приложений окна приложения. Можно впринципе сделать и 
# графический интерфейс но вряд ли это будет выглядить хорошо.
# Поискать библиотеки для красивого вывода информации.


filename = settings.GoalManagerFileName
goal_array = []
rand10_array = []

# Objects to be stored in the file
class Goal:
    def __init__(self, name, status):
        self.status = status
        self.name = name


def save(filename, goals): # goals are array
    with open(filename, "wb") as f:
        pickle.dump(goals, f)

def load(filename):
    with open(filename, "rb") as f:
        loaded_goals = pickle.load(f)
    return loaded_goals # return array

def add(goal):
    goal_array.append(goal)

def remove(index):
    goal_array.pop(int(index))

def randmode():
    rand10_array.clear()
    for x in range(10):
        rand = random.randint(0, len(goal_array)-1)
        rand10_array.append(rand)

load(filename)

defmode = True
rand10mode = False

while(True):
    
    os.system('cls' if os.name == 'nt' else 'clear')

    if (defmode):
        for x, i in enumerate(goal_array):
            if (i.status == "ongoing"): 
                print(f"%d  %s" % (x, i.name))

    if (rand10mode):
        randmode()
        for x, i in enumerate(goal_array):
            if (i.status == "ongoing" and rand10_array.count(x) > 0): 
                print(f"%d  %s \n" % (x, i.name))

    com = input("Enter a command: ")
    match com:
        case "load":
            goal_array = load(filename)
        case "save":
            save(filename, goal_array)

        case "add":
            inp = input("Enter a name: ")
            goal = Goal(inp, "ongoing")
            add(goal)

        case "remove":
            inp = input("Index to remove: ")
            remove(inp)
        
        case "help":
            print("help, load, save, add, remove, exit, invert, randm, defm")

        case "invert":
            goal_array = goal_array[::-1]

        case "randm":
            defmode = False
            rand10mode = True

        case "defm":
            defmode = True
            rand10mode = False

        case "exit":
            quit()

    