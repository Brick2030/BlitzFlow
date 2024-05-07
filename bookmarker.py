import settings
import pickle
import datetime
import time
import os
from prettytable import PrettyTable
import subprocess



example = "https://suckless.org/sucks/systemd/"
filename = settings.SaveDirectory + settings.BookMarkFileName

bm_array = [] # Main array for all bookmarks. Will be saved and loaded.


class bookmark:
    def __init__(self, link, description, date, isUp):
        self.link = link
        self.description = description
        self.date = date
        self.isUp = isUp

def simplify_link(link: str):
    try:
        link_parts = link.split('/')
        simplified_link = link_parts[2].split('.')
        return simplified_link[len(simplified_link)-2]
    except:
        return link



def showList(arrayName):
    BookTab = PrettyTable()
    BookTab.clear()
    BookTab = PrettyTable(['Index', 'Link','Description', 'When added', 'Is Up?'])
    BookTab.align = "r"

    for x, i in enumerate(arrayName):
        simpleLink = simplify_link(i.link)
        BookTab.add_row([x, simpleLink, i.description, str(i.date), str(i.isUp)])
    print(BookTab)


def save(filename): # Saving array of bookmarks into file
    with open(filename, "wb") as f:
        pickle.dump(bm_array, f)

def load(filename): # Loads array of bookmarks from file
    with open(filename, "rb") as f:
        bm_array = pickle.load(f)
    return bm_array # return array

def add(bookmark):
    bm_array.append(bookmark)

def remove(index):
    bm_array.pop(int(index))

def copy_clipboard(msg):

    with subprocess.Popen(['xclip','-selection', 'clipboard'], stdin=subprocess.PIPE) as pipe:
        pipe.communicate(input=msg.encode('utf-8'))

def select(index):
    link = bm_array[int(index)].link
    copy_clipboard(link)
    print("Copied!")
    time.sleep(2)



while(True):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    showList(bm_array)
    
    com = input("Enter a command: ")
    match com:
        case "add":
            inp_link = input("Input a link: ")
            inp_descr = input("Description: ")
            inp_date = current_date = datetime.date.today().strftime("%d-%m-%Y")
            inp_isUp = True
            bm = bookmark(inp_link, inp_descr, inp_date, inp_isUp)
            add(bm)
        case "remove":
            inp = input("Index to remove: ")
            remove(inp)

        case "save":
            save(filename)

        case "load":
            bm_array = load(filename)

        case "select":
            inp = input("Index to select: ")
            select(int(inp))


