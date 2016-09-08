#!/usr/bin/python3
from tkinter import *
import subprocess


BROWN_TIMES=0
START_STOP=False

def funct1():
    top = Toplevel()
    top.title("About this application...")
    top.grab_set()
    global BROWN_TIMES
    msg = Message(top, text="# times Brown has been pressed   "+str(BROWN_TIMES))
    msg.pack()

    button = Button(top, text="Dismiss", command=top.destroy)
    button.pack()


def funct2():
    n = subprocess.check_output("ssh root@canada.sendotux.net 'pwd'", shell=True)
    print(n.decode("utf-8"))

def funct3():
    global BROWN_TIMES
    BROWN_TIMES += 1

def funct4():
    global START_STOP
    if START_STOP:
        top = Toplevel()
        top.title("START")
        top.grab_set()
        msg = Message(top, text="UH")
        msg.pack()

        button = Button(top, text="Dismiss", command=top.destroy)
        button.pack()    
        START_STOP = False
    else:
        top = Toplevel()
        top.title("STOP")
        top.grab_set()
        msg = Message(top, text="LOL")
        msg.pack()

        button = Button(top, text="Dismiss", command=top.destroy)
        button.pack()    
        START_STOP = True


root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red", command=funct4)
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown", command=funct3)
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue", command=funct2)
bluebutton.pack( side = LEFT )



blackbutton = Button(bottomframe, text="Black", fg="black", command=funct1)
blackbutton.pack( side = BOTTOM)



root.mainloop()
