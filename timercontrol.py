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
    com = input()
    
    match com:
        case "add":
            cycles = input("cycles: ")
            name = input("name: ")
            add(cycles, name, 1, 0)

        case "show all":
            for i in taskList:
                print(i.ReturnTask())

        case "complete":
            index = input("Index to complete: ")
            time = input("How many cycles used to finish: ")
            complete(int(index), (time))

        case "fail":
            index = input("Index to fail: ")
            fail(int(index))

        case "remove":
            index = input("Index to remove")
            remove(int(index))
