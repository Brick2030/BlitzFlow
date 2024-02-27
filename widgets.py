from random import randint

class obj():
    
    def rand_quote(self): # Returns random quote from file
         
        qfile = open("quotes")
        wholetext = qfile.read()
        qfile.close()

        textchunk = wholetext.split('#') # Textchunk is quote + author. Separated by #
        num = randint(0, len(textchunk)-1) # random number 
        quote = textchunk[num].split('$')  # Quote is [0] text and [1] is author
        # Dont put # at the end of file. It will break everything. (Fix it)
        # Formated output
        # (It's better to use return?)
        return (quote[1] + " (" + str(num) + ")\n" + quote[0])

        #print(quote[1])
        #print("-")
        #print(quote[0])



    def line(self):
        print("-----------------------------------------------------------------------------")
