import timer
import os
import time
import tasks


taskList = []

def add(cycles, name, status, result):
    task1 = tasks.task(cycles, name, status, result)
    taskList.append(task1)

def remove(index):
    taskList.pop(index)

def complete(index, time):
    taskList[index].ChangeStatus(3)
    taskList[index].ChangeResult(time)

def fail(index):
    taskList[index].ChangeStatus(0)


while(True):
    os.system('cls' if os.name == 'nt' else 'clear')
    for x, i in enumerate(taskList):
        if (i.ReturnTask()[2] == "Nothing" or i.ReturnTask()[2] == "Ongoing"):
            print(x, " ", i.ReturnTask())
    print("- - -")
    for x, i in enumerate(taskList):
        if(i.ReturnTask()[2] == "Completed"):
            print(x, " ", i.ReturnTask())

    com = input()
    
    match com:
        case "add":
            cycles = input("cycles: ")
            name = input("name: ")
            add(cycles, name, 1, 0)

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

        case "help":
            print("\nadd\nfinish\nfail\nremove\nhelp\nexit\n")
            i = input("type anything to close help: ")
