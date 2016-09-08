#!/usr/bin/python3
from tkinter import *
import subprocess

class MainWindow(object):
    def __init__(self):
        self.__root = Tk()
        self.__root.geometry(self.__center_window(400, 200))
        self.__root.title("tkinter class test")
        self.__root.mainloop()

    def __center_window(self, win_width, win_height):
        scr_width=self.__root.winfo_screenwidth()
        scr_height=self.__root.winfo_screenheight()
        xpos = int(scr_height/2 - win_height/2)
        ypos = int(scr_width/2 - win_width/2)
        geometry=str(win_width)+"x"+str(win_height)+"+"+ypos+"+"+xpos
        return geometry

if __name__ == "__main__":
    win = MainWindow()
