from tkinter import *
from time import *
from math import *
tk = Tk()
screen = Canvas(tk, width=800,height=800, background="white")
screen.pack()

##Reference shapes - Triangle + 3 Circles

#screen.create_polygon(400, 250, 300, 423.21, 500, 423.21, fill = "black")
#screen.create_oval(100,223.21,500,623.21)
#screen.create_oval(300,223.21,700,623.21)
#screen.create_oval(200,50,600,450)

#Creation of 3 arcs
screen.create_arc(100,223.21,500,623.21, start = 0, extent = 60, fill = "hotpink", outline = "hotpink")
screen.create_arc(300,223.21,700,623.21, start = 120, extent = 60, fill = "hotpink", outline = "hotpink")
screen.create_arc(200,50,600,450, start = 240, extent = 60, fill = "hotpink", outline = "hotpink")

