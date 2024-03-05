import timer
import os
import time
import tasks
import widgets
import cycles


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




quote = widgets.info()






while(True):
    os.system('cls' if os.name == 'nt' else 'clear')

    print(quote.rand_quote(), "\n")

    slp = cycles.returnCycles()
    print("Cycles until sleep:", slp)
    print("%7s %10s %40s %10s %10s" % ("[Index]", "[Cycles]", "[Name]", "[Status]", "[Result]"))




    for x, i in enumerate(taskList):
        array = i.ReturnTask()


        if (array[2] == "Nothing" or array[2] == "Ongoing"):
            print("%7s %10s %40s %10s %10s" % (str(x), str(array[0]), array[1], array[2], str(array[3])))
    print("- - -")
    
    for x, i in enumerate(taskList):
        array = i.ReturnTask()
        if(array[2] == "Completed"):
            print("%7s %10s %40s %10s %10s" % (str(x), str(array[0]), array[1], array[2], str(array[3])))

    com = input()
    
    match com:
        case "add":
            ccycles = input("cycles: ")
            name = input("name: ")
            add(ccycles, name, 1, 0)

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
