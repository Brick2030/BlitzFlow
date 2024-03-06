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

def move(index, index2):
    tempObj = taskList[index2]
    taskList[index2] = taskList[index]
    taskList[index] = tempObj



quote = widgets.info() # Object for quote.









while(True):
    os.system('cls' if os.name == 'nt' else 'clear')

    print(quote.rand_quote()) # Random Quote.

    slp = cycles.returnCycles() # How many cycles until sleep time.
    print("Cycles until sleep:", slp, "\n")
    print("%7s %10s %40s %10s %10s %20s" % ("[Index]", "[Cycles]", "[Name]", "[Status]", "[Result]", "[Result 2]")) # Header format.


    cycleSumm = 0 # Summ of cycles.
    for x, i in enumerate(taskList): # This loop outputs tasks that need to be solved rn.
        array = i.ReturnTask() # Array = one task. It's array bc it returns array.


        if (array[2] == "Nothing" or array[2] == "Ongoing"):
            cycleSumm = cycleSumm + int(array[0])
            print("%7s %10s %40s %10s %10s %20s" % (str(x), str(array[0]), array[1], array[2], str(array[3]), "NO RESULT"))
   


    print("- - - "*20)
    print("%10s" % ("Summ: "), cycleSumm)
    print("- - - "*20)
    
    for x, i in enumerate(taskList): # Second table for completed tasks
        array = i.ReturnTask() # array = task. 
        if(array[2] == "Completed"):
            print("%7s %10s %40s %10s %10s %20s" % (str(x), str(array[0]), array[1], array[2], str(array[3]), str(float(array[3])/float(array[0])*100)), "%")


    com = input() # Command input
    
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

        case "move":
            index = input("Enter index of task to move")
            index2 = input("Enter index where to move")
            move(int(index), int(index2))
            


        case "help":
            print("\nadd\nfinish\nfail\nremove\nhelp\nexit\nmove\n")
            i = input("type anything to close help: ")
