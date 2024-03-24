import pickle
import os
import settings

filename = settings.GoalManagerFileName
goal_array = []


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


while(True):
    
    os.system('cls' if os.name == 'nt' else 'clear')

    
    for x, i in enumerate(goal_array):
        if (i.status == "ongoing"): 
            print(f"%d  %s - %s" % (x, i.name, i.status))

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
            print("help, load, save, add, remove, exit")

        case "exit":
            quit()

    