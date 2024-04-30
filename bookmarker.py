import settings
import pickle
import datetime
import time
import os
from prettytable import PrettyTable
import subprocess

filename = settings.SaveDirectory + settings.BookMarkFileName

# --- Базовый миннимум ---
# Добавить сразу шифрование AES. (потом)
# Упрощение ссылки на вывод до самого сайта без деталей.
# Можно настроить вывод рандомных 10 ссылок.
# Ввести поиск (по всей программе?) в которой на ввод слово, а на выходе все индексы.

# --- Повыешние удобства и безопасности ---
# Автоматическая проверка работают ли ссылки?
# Настроить так же валидацию ввода и защиту от ошибок ввода по всей программе в целом.
# Стоит ли ввести какой то уровень API для всей программы в целом? Изучить вопрос централизации.
# При этом централизация не должна ударять по скорости и удобству взаимодействия
# Для публикации этого ПО нужно сделать его в целом более полезным для масс, более настраиваемым.

# Создание отдельного листа для вышедших из строя сайтов.

bm_array = [] # Main array for all bookmarks. Will be saved and loaded.


class bookmark:
    def __init__(self, link, description, date, isUp):
        self.link = link
        self.description = description
        self.date = date
        self.isUp = isUp

def showList(arrayName):
    BookTab = PrettyTable()
    BookTab.clear()
    BookTab = PrettyTable(['Index', 'Link','Description', 'When added', 'Is Up?'])
    BookTab.align = "r"

    for x, i in enumerate(arrayName):
        BookTab.add_row([x, i.link, i.description, str(i.date), str(i.isUp)])
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





# Copy some text to the clipboard



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


