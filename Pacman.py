from tkinter import *
from time import *
from math import *
tk = Tk()
screen = Canvas(tk, width=800,height=800, background="black")
screen.pack()

#setting up the distance, radius, speed for pacman
d = 200
r = d/2
xSpeed = 10

#measurements for pacman
x1 = -300
y1 = 300

x2 = x1 + d
y2 = y1 + d

#measurements for centerpoint
x3 = x1 + r
y3 = y1 + r

#measurements for player text
x4 = x3
y4 = y2 + 20

#measurements for eyes
x5 = -250
y5 = 350

x6 = x5 + 50
y6 = y5 + 50

#measurements for ghost's arc shape
x7 = x1 - 300
y7 = y1

x8 = x7 + d
y8 = y7 + d

#measurements for ghost's box shape
x9 = x7
y9 = y1 + r

x10 = x9 + r 
y10 = y9 + r 

#measurements for ghost eye 1
x11 = x7 + 30
y11 = y7 + 30

x12 = x11 + r/2
y12 = y11 + r/2

#measurements for ghost eye 2
x13 = x11 + r
y13 = y11

x14 = x13 + r/2
y14 = y13 + r/2

#measurements for ghost text
x15 = x7 + r
y15 = y10 + 20

#measurements for pacman title text
x16 = 400
y16 = 100

#arrays for different angles
modelstop = [30, 25, 20, 15, 10, 5]
modelsbottoms = [300, 315, 325, 335, 345, 355]

dots = [1,2,3,4,5,6,7,8,9,10,11]
dotXValues = [0,0,0,0,0,0,0,0,0,0,0]

#creates walls
screen.create_line(0, 250, 800, 250, fill = "blue", width = "30")
screen.create_line(0, 550, 250, 550, fill = "blue", width = "30")
screen.create_line(550, 550, 800, 550, fill = "blue", width = "30")
screen.create_line(235, 550, 235, 800, fill = "blue", width = "30")
screen.create_line(565, 550, 565, 800, fill = "blue", width = "30")


#creates dots
for b in range(11):

    X1 = 100 + 100*b
    dotXValues[b] = X1
    Y1 = 390

    X2 = X1 + 20
    Y2 = Y1 + 20

    dots[b] = screen.create_oval(X1, Y1, X2, Y2, fill = "white")
print(dotXValues)

i = 0


#creating/animating pacman
for f in range(1500):

    msn = f % 6

    pacman = screen.create_arc( x1, y1, x2, y2, start= modelstop[msn], extent= modelsbottoms[msn], fill="yellow")
    #center = screen.create_oval(x3, y3, x3, y3, fill = "white", width = "5")
    player = screen.create_text(x4, y4, text = "PLAYER 1", font = "System 20", fill = "white")
    eye = screen.create_oval(x5, y5, x6, y6, fill = "black", outline = "white", width = "20")
    ghostarc = screen.create_arc(x7, y7, x8, y8, start = 0 , extent = 180, fill = "pink")
    ghostbox = screen.create_rectangle(x9, y9, x10, y10, fill = "pink", outline = "pink")
    ghosteye1 = screen.create_oval(x11, y11, x12, y12, fill = "black", outline = "white", width = "20")
    ghosteye2 = screen.create_oval(x13, y13, x14, y14, fill = "black", outline = "white", width = "20")
    ghosttext = screen.create_text(x15, y15, text = "PINKY", font = "System 20", fill = "white")
    title = screen.create_text(x16, y16, text = "WELCOME TO PACMAN", font = "System 40", fill = "white")

    screen.update()
    sleep(0.03)
    screen.delete(pacman, player, eye, ghostarc, ghostbox, ghosteye1, ghosteye2, ghosttext)


    #updating values
    x1 = x1 + xSpeed

    x2 = x1 + d

    x3 = x1 + r

    x4 = x3

    x5 = x5 + xSpeed

    x6 = x5 + 50

    x7 = x7 + xSpeed

    x8 = x7 + d

    x9 = x7 

    x10 = x9 + d

    x11 = x11 + xSpeed

    x12 = x11 + r/2

    x13 = x13 + xSpeed
    
    x14 = x13 + r/2

    x15 = x15 + xSpeed

    distance = sqrt((x3 - x1)**2 + (y3 - y1)**2)

    if x1 > dotXValues[i]:
        screen.delete(dots[i])
        i = i + 1

    
    
   

    

    



