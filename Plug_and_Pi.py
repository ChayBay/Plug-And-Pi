from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from PIL import Image,ImageTk
import tkinter as tk
import hangman
import collect
import snake
import threading

root = tk.Tk()
root.title("Plug and Pi")
root.geometry('1920x1080')

bigPi=(Image.open("BigPiBk.png"))
reBigPi = bigPi.resize((root.winfo_screenwidth(),root.winfo_screenheight()),Image.ANTIALIAS)
newBigPi = ImageTk.PhotoImage(reBigPi)

smallPi=(Image.open("SmallPiBk.png"))
reSmallPi = smallPi.resize((root.winfo_screenwidth(),root.winfo_screenheight()),Image.ANTIALIAS)
newSmallPi = ImageTk.PhotoImage(reSmallPi)

Label(root, image = newBigPi, width = root.winfo_screenwidth(), height = root.winfo_screenheight()).place(relx=0.5, rely=0.5, anchor=CENTER)


root.configure(bg='green')
root.columnconfigure((0,1,2), weight = 1)
root.rowconfigure((0,1,2), weight = 1)
root.attributes('-fullscreen', True)

players = []
f = open("players.txt",'r')
for x in f:
    players.append(x.rstrip())
f.close()


def kill():
    root.destroy()
def run_hang():
    hangman.main(1,user_list.get())

def run_collect():
    collect.main(1,user_list.get())

def run_snake():
    snake.main(1,user_list.get())

def createDrop(dd):
    dd.destroy()
    players = []
    f = open("players.txt",'r')
    for x in f:
        players.append(x.rstrip())
    f.close()
    dropNew = tk.OptionMenu(userFrame, user_list, *players)
    dropNew.config(width=6, height=1, font=('Helvetica',10), bg="black", fg="white")
    dropNew.grid(column = 2, row = 0)

def new_user(new_name):
    f=open("playerSaves/"+new_name + "_collect.txt",'a')
    f.close()
    f=open("playerSaves/"+new_name + "_hang.txt",'a')
    f.close()
    f=open("playerSaves/"+new_name + "_snake.txt",'a')
    f.close()
    f=open("players.txt",'a')
    f.write("\n")
    f.write(new_name)
    f.close()
    nameEntered.delete(0, "end")
    
    createDrop(drop)
    Label(userFrame, text="New user created!", font = "white").grid(column = 2, row = 1, sticky = "n")

midFrame = LabelFrame(root, bg = "orange", width = root.winfo_screenwidth()/1.2, height = root.winfo_screenheight()/1.2, borderwidth = 0, highlightthickness = 0)
midFrame.grid(column = 1, row = 1, sticky = "nesw")
midFrame.grid_propagate(False)
midFrame.columnconfigure(0, weight=6) #title column
midFrame.columnconfigure(1, weight=4) #games column
midFrame.rowconfigure((0,1,2,3), weight = 1)


plugFrame = LabelFrame(midFrame, width = 700, height = midFrame.winfo_screenheight(), bg = "white", borderwidth = 0, highlightthickness = 0)
plugFrame.grid(column = 0, row = 0, rowspan = 4, sticky = "nesw")
plugFrame.grid_propagate(False)
plugPiImg=(Image.open("plugPi.png"))
rePlugPi = plugPiImg.resize((int(plugFrame.winfo_screenwidth()/1.7),int(plugFrame.winfo_screenheight())),Image.ANTIALIAS)
newPlugPi = ImageTk.PhotoImage(rePlugPi)
#Label(plugFrame, image = newSmallPi, width = root.winfo_screenwidth(), height = root.winfo_screenheight()).place(relx=0.5, rely=0.5, anchor=CENTER)
Button(plugFrame, image = newPlugPi, borderwidth = 0, highlightthickness = 0, command = lambda : kill()).place(relx=0.5, rely=0.5, anchor=CENTER)


userFrame = LabelFrame(midFrame, width = 300, height = 50, bg = "black", borderwidth = 0, highlightthickness = 0)
userFrame.columnconfigure((0, 2), weight=1)
userFrame.rowconfigure(0, weight = 1)
userFrame.rowconfigure(1, weight = 1)
userFrame.grid(column = 1, row = 0, sticky = "nesw")
userFrame.grid_propagate(False)

Label(userFrame, image = newSmallPi, width = root.winfo_screenwidth(), height = root.winfo_screenheight()).place(relx=0.5, rely=0.5, anchor=CENTER)
Label(userFrame, text = "Select or Enter New User:", bg="black", fg="white").grid(column = 0, row = 0, columnspan = 2)

user_list = tk.StringVar()
user_list.set(players[0])
drop = tk.OptionMenu(userFrame, user_list, *players)
drop.config(width=6, height=1, font=('Helvetica',10), bg="black", fg="white")
drop.grid(column = 2, row = 0)

new_name = tk.StringVar()
nameEntered = ttk.Entry(userFrame, width=15, textvariable = new_name)
nameEntered.grid(column = 0, row = 1, sticky = "n")
Button(userFrame, text = "Create New User", bg="black", fg="white", command = lambda : new_user(new_name.get())).grid(column = 1, row = 1, sticky = "n")


colectFrame = LabelFrame(midFrame, width = 300, height = 200, bg = "white", borderwidth = 0, highlightthickness = 0)
colectFrame.grid(column = 1, row = 1, sticky = "nesw")
colectFrame.grid_propagate(False)
colectImg=(Image.open("colectGame.png"))
reColect = colectImg.resize((int(colectFrame.winfo_screenwidth()/3.3)+3,int(colectFrame.winfo_screenheight()/3.9)+2),Image.ANTIALIAS)
newColect = ImageTk.PhotoImage(reColect)
Label(colectFrame, image = newSmallPi, width = root.winfo_screenwidth(), height = root.winfo_screenheight()).place(relx=0.5, rely=0.5, anchor=CENTER)
Button(colectFrame, image = newColect, borderwidth = 0, highlightthickness = 0, command = lambda : threading.Thread(target=run_collect).start()).place(relx=0.5, rely=0.5, anchor=CENTER)


snakeFrame = LabelFrame(midFrame, width = 300, height = 200, bg = "white", borderwidth = 0, highlightthickness = 0)
snakeFrame.grid(column = 1, row = 2, sticky = "nesw")
snakeFrame.grid_propagate(False)
snakeImg=(Image.open("snakeGame.png"))
reSnake = snakeImg.resize((int(colectFrame.winfo_screenwidth()/3.3)+3,int(colectFrame.winfo_screenheight()/3.9)+2),Image.ANTIALIAS)
newSnake = ImageTk.PhotoImage(reSnake)
Label(snakeFrame, image = newSmallPi, width = root.winfo_screenwidth(), height = root.winfo_screenheight()).place(relx=0.5, rely=0.5, anchor=CENTER)
Button(snakeFrame, image = newSnake, borderwidth = 0, highlightthickness = 0, command = lambda : threading.Thread(target=run_snake).start()).place(relx=0.5, rely=0.5, anchor=CENTER)


hangFrame = LabelFrame(midFrame, width = 300, height = 200, bg = "white", borderwidth = 0, highlightthickness = 0)
hangFrame.grid(column = 1, row = 3, sticky = "nesw")
hangFrame.grid_propagate(False)
hangImg=(Image.open("hangGame.png"))
reHang = hangImg.resize((int(colectFrame.winfo_screenwidth()/3.3)+3,int(colectFrame.winfo_screenheight()/3.9)+2),Image.ANTIALIAS)
newHang = ImageTk.PhotoImage(reHang)
Label(hangFrame, image = newSmallPi, width = root.winfo_screenwidth(), height = root.winfo_screenheight()).place(relx=0.5, rely=0.5, anchor=CENTER)
Button(hangFrame, image = newHang, borderwidth = 0, highlightthickness = 0, command = lambda : threading.Thread(target=run_hang).start()).place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
