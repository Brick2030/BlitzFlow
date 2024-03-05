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



        #textchunk = wholetext.split('#') # Textchunk is quote + author. Separated by #
        #num = randint(0, len(textchunk)-1) # random number 
        #quote = textchunk[num].split('$')  # Quote is [0] text and [1] is author
        # Dont put # at the end of file. It will break everything. (Fix it)
        #return (quote[0] + " (" + str(num) + ")\n" + quote[1])



    def line(self):
        print("- - - - - - - - - - - - - - - - - - - - - - - -")



class taskmanager(): # Simple to-do list
    def add(self):
        print("nothing")



class datemanager(): # Reminders and stuff

    def today(self):
        print(ctime())
