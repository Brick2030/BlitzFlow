import timer
import os
import time



print("Welcome to Cycles Timer:\n")

timerObject = timer.Timer() # This object will be controlled by commands
#timerObject.ShowCycles() 

#print("Enter command to continue: ")

while(True):
    time.sleep(0.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    timerObject.ShowCycles()
    command = input("Enter command to continue:\n")

    match command:
        case "exit":
            quit()

        #case _:
            #print("Error! Wrong command!\n")

        case "add":
            print("Enter planned cycles for task:")
            plan = input()
            print("Enter name of the task")
            name = input()
            timerObject.AddTask(plan, name)






        case _:
            print("Wrong command!\n")


