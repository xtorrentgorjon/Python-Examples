#!/usr/bin/python3
from tkinter import *
import subprocess

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

def funct2():
    n = subprocess.check_output("ssh root@canada.sendotux.net 'pwd'", shell=True)
    print(n.decode("utf-8"))

bluebutton = Button(frame, text="Blue", fg="blue", command=funct2)
bluebutton.pack( side = LEFT )

def funct1():
    top = Toplevel()
    top.title("About this application...")
    top.grab_set()

    msg = Message(top, text="about_message")
    msg.pack()

    button = Button(top, text="Dismiss", command=top.destroy)
    button.pack()

blackbutton = Button(bottomframe, text="Black", fg="black", command=funct1)
blackbutton.pack( side = BOTTOM)



root.mainloop()
