from tkinter import *
from time import *
from math import *
from random import *
tk = Tk()
screen = Canvas(tk, width=1000,height=1000, background="ivory3")
screen.pack()

#Text
screen.create_text(175, 100, text = "Sweat Now", font = "verdana 40", fill = "Royalblue2")
screen.create_text(825, 100, text = " Shine Later", font = "verdana 40", fill = "Goldenrod")

#Sweatdrops
screen.create_polygon(100,150,75,200,75,250,125,250,125,200,100,150, fill = "Skyblue", outline = "blue", smooth = "true")
screen.create_polygon(175,125,150,150,150,200,200,200,200,150,175,125, fill = "Skyblue", outline = "blue", smooth = "true")

#Trophy
screen.create_arc(775,180,800,210, start = 180, extent = 180, fill = "goldenrod", outline = "goldenrod")
screen.create_arc(850,180,875,210, start = 180, extent = 180, fill = "goldenrod", outline = "goldenrod")
screen.create_arc(790,135,860,225, start = 180, extent = 180, fill = "gold", outline = "gold")
screen.create_rectangle(810,225,840,250, fill = "gold", outline = "gold")
screen.create_line(800,250,850,250,fill = "goldenrod", width = "10")


###Court + 3point line

x1 = 0
x2 = randint(25,100)
y1 = 450
y2 = y1 + 25
    
for r1 in range(230):
    if y2 >1025:
            y2 = 1025
     
    for r in range(21):
            if x2 > 1025:
                    x2 = 1025

            screen.create_rectangle(x1,y1,x2,y2, fill = "burlywood3")
     
            x1 = x2
            randLen = randint(25,100)
            x2 = x1 + randLen

    x1 = 0
    x2 = randint(25,100)
    y1 = y2
    y2 = y2 + 25


screen.create_arc(-600,125,1600,870, start = 180, extent = 180, width = "10")
screen.create_arc(225,630,775,870, start = 180, extent = 180, width = "10")
screen.create_line(300,500,225,750,775,750,700,500,width = "10")



#Small lines beside the paint (right)
screen.create_line(760,700,790,700, width = "10")
screen.create_line(740,650,775,650, width = "10")
screen.create_line(730,600,760,600, width = "10")
screen.create_line(715,550,745,550, width = "30")

#Small lines beside the paint(left)
screen.create_line(210,700,240,700, width = "10")
screen.create_line(225,650,260,650, width = "10")
screen.create_line(240,600,270,600, width = "10")
screen.create_line(255,550,285,550, width = "30")

#NetBeam, Backboard
screen.create_rectangle(485,0,515, 50, fill = "gainsboro")
screen.create_rectangle(475,50,525,220, fill = "grey81", outline = "black", width = "3")
screen.create_line(350,50,350,250,650,250,650,50,350,50, fill = "black", width = 8)
screen.create_rectangle(485,225,515,250, fill = "orangered")
screen.create_line(460,160,460,225,540,225,540,160,460,160, fill = "white", width = "5")

#mats
x5 = 0
x6 = x5 + 100

y5 = 265
y6 = 425

while x6 <= 1000:
    screen.create_rectangle(x5,y5,x6,y6, fill = "skyblue3", outline = "black", width = "5")

    x5 = x6
    x6 = x5 + 100

#Net
x3 = 460
x4 = x3 + 10
y3 = 210
y4 = y3 + 10
c = 0
while y4 < 285:

    while x4 < (540 - 2.5*c):

        screen.create_oval(x3,y3,x4,y4, outline = "white", width = "3")
     
        x3 = x4
        x4 = x4 + 10

        if x4 > 540 - 2.5*c:
            x4 = 540 - 2.5*c

    x3 = 460 + (5*c)
    x4 = x3 + 10
    y3 = y4
    y4 = y3 + 10
    c = c + 1

screen.create_oval(460,210,540,225, outline = "orangered", width = "5")



###Grid lines
##spacing = 50
##
##for x in range(0, 1000, spacing):
##  screen.create_line(x, 25, x, 1000, fill="white")
##  screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N, fill = "white")
##
##for y in range(0, 1000, spacing):
##  screen.create_line(25, y, 1000, y, fill="white")
##  screen.create_text(5, y, text=str(y), font="Times 9", anchor = W, fill = "white")










