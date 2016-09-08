#!/usr/bin/python3
from tkinter import *
import subprocess


class TableWindow(object):
    def __init__(self):
        self.__table_values = []
        self.__table_height = 5
        self.__table_width = 5

        self.__top = Toplevel()
        self.__top.title("CELLS")
        self.__top.grab_set()
        self.__frame1 = Frame(self.__top)
        self.__frame1.pack()
        self.__frame2 = Frame(self.__top)
        self.__frame2.pack()

        for i in range(self.__table_height*self.__table_width):
            self.__table_values.append([Entry(self.__frame1),str(i)])

    def __print_table(self):
        for i in range(self.__table_height): #Rows
            for j in range(self.__table_width): #Columns
                b = self.__table_values[i*self.__table_height+j][0]
                #print(values[i*height+j])
                b.delete(0, END)
                b.insert(0, self.__table_values[i*self.__table_height+j][1])
                b.grid(row=i, column=j)


    def create_window(self):
        self.__print_table()
        blackbutton = Button(self.__frame2, text="Table", fg="black", command=self.__button)
        blackbutton.pack( side = BOTTOM)     

    def __button(self):
        print(self.__table_values)
        for i in range(self.__table_height*self.__table_width):
            print(self.__table_values[i][0].get())
            self.__table_values[i][1] = self.__table_values[i][0].get()
        print(self.__table_values)
        self.__top.destroy()

class MainWindow(object):
    def __init__(self):
        self.__n = TableWindow()
        pass

    def create_window(self, sizex=400, sizey=200):
        self.__root = Tk()
        self.__root.geometry(self.__center_window(sizex, sizey))
        self.__root.title("tkinter class test")

        blackbutton = Button(self.__root, text="Table", fg="black", command=self.__button)
        blackbutton.pack( side = BOTTOM)
        self.__root.mainloop()

    def __center_window(self, win_width, win_height):
        scr_width=self.__root.winfo_screenwidth()
        scr_height=self.__root.winfo_screenheight()
        xpos = int(scr_height/2 - win_height/2)
        ypos = int(scr_width/2 - win_width/2)
        geometry="%sx%s+%s+%s" % (win_width, win_height, ypos, xpos)
        return geometry

    def __button(self):
        self.__n.create_window()

if __name__ == "__main__":
    win = MainWindow()
    win.create_window()
