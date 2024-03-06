from random import randint
from time import ctime

class info(): # Static info without interaction
    
    def rand_quote(self): # Returns random quote from file
         
        qfile = open("quotes")
        wholetext = qfile.read()
        qfile.close()

       

        BlockByAuthor = wholetext.split('#')
        randnum1 = randint(0, len(BlockByAuthor)-1)
        ArrayByAuthor = BlockByAuthor[randnum1].split('$')
        authorName = ArrayByAuthor[0].replace("\n", "")
        randnum2 = randint(1, len(ArrayByAuthor)-1)
        authorQuote = ArrayByAuthor[randnum2].replace("\n", "").replace("*", "\n")

        
        return(authorName + "\n" + authorQuote + "\n")

 
    def delayed_tasks(self):
        return 0


    def line(self):
        print("- - - - - - - - - - - - - - - - - - - - - - - -")



class taskmanager(): # Simple to-do list
    def add(self):
        print("nothing")



class datemanager(): # Reminders and stuff

    def today(self):
        print(ctime())
