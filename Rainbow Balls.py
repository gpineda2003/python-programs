
from tkinter import *
from time import *
from math import *
from random import *
tk = Tk()
screen = Canvas(tk, width=800,height=800, background="black")
screen.pack()

#ESTABLISHING DIAMETER AND RADIUS
d = 800
r = d/2

#PRINTING THE TARGET
for c in range(7):

    x1 = 400 - r
    x2 = 400 + r
    y1 = x1
    y2 = x2
    
    screen.create_oval(x1, y1, x2, y2, outline = "white")    

    r = r - 66.67

#INITIAL VALUES
d = 50

    
x1 = 350
y1 = 350
x2 = x1 + d
y2 = y1 + d
x3 = x1 + d/2
y3 = y1 + d/2

xSpeed = 7
ySpeed = 7
currentColor = "black"

#CREATING BALL AND CENTERPOINT
for f in range(8000): 
    ball = screen.create_oval(  x1,  y1,  x2,  y2,  fill= currentColor) 
    center = screen.create_oval (x3, y3, x3, y3, fill = "orange", width = "5")
   
    screen.update()
    sleep(0.03)
    screen.delete( ball, center )

    #Update positions before the next frame
    x1 = x1 + xSpeed  
    y1 = y1 + ySpeed

    x2 = x1 + d
    y2 = y1 + d

    x3 = x1 + d/2
    y3 = y1 + d/2


    #CALCULATE THE DISTANCE BETWEEN BALL CENTERPOINT AND CENTER OF TARGET
    distance = sqrt((400-x3)**2 + (400-y3)**2)


    #CHANGE OF DIRECTIONS OR SPEED
    if x2 > 800:
        xSpeed = -1 * xSpeed + randint(-10,10)
        if xSpeed > 0:
            xSpeed = xSpeed * -1

    if x1 < 0:
        xSpeed = -1 * xSpeed + randint(-10,10)
        if xSpeed < 0:
            xSpeed = xSpeed * -1
    if y1 < 0:
        ySpeed = -1 * ySpeed + randint(-10,10)
        if ySpeed < 0:
            ySpeed = ySpeed * -1

    if y2 > 800:
        ySpeed = -1 * ySpeed + randint(-10,10)
        if ySpeed > 0:
            ySpeed = ySpeed * -1


    #CHANGE OF COLORS
    if 0 < distance <= 66.67:
        currentColor = "red"

    elif 66.67 < distance <= 133.34:
        currentColor = "orange"

    elif 133.34 < distance <= 200.01:
        currentColor = "yellow"

    elif 200.01 < distance <= 266.68:
        currentColor = "green" 

    elif 266.68 < distance <= 333.35:
        currentColor = "blue"

    elif 333.35 < distance <= 400.02:
        currentColor = "purple"

    else:
        currentColor = "grey"

###GRID FOR MEASUREMENTS
##spacing = 50
##
##for x in range(0, 1000, spacing): 
##    screen.create_line(x, 25, x, 1000, fill="blue")
##    screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N, fill ="white")
##
##for y in range(0, 1000, spacing):
##    screen.create_line(25, y, 1000, y, fill="blue")
##    screen.create_text(5, y, text=str(y), font="Times 9", anchor = W, fill ="white")
##
##screen.update()
