from math import *
from tkinter import *
from time import *
from random import *
myInterface = Tk()
screen = Canvas( myInterface, width=800, height=800, background="#704e78" )
screen.pack()

#IMPORTING IMAGES ########################################################################################################################################
slash1 = PhotoImage(file="idle.gif")
slash2 = PhotoImage(file="slash1.gif")
slash3 = PhotoImage(file="slash2.gif")
slash4 = PhotoImage(file="slash3.gif")

run1 = PhotoImage(file="run1.gif")
run2 = PhotoImage(file="run2.gif")
run3 = PhotoImage(file="run3.gif")
run4 = PhotoImage(file="run4.gif")
run5 = PhotoImage(file="run5.gif")
run6 = PhotoImage(file="run6.gif")
run7 = PhotoImage(file="run7.gif")
run8 = PhotoImage(file="run8.gif")

#Arrays 
run = []

run.append(run1)
run.append(run2)
run.append(run3)
run.append(run4)
run.append(run5)
run.append(run6)
run.append(run7)
run.append(run8)

slash = []

slash.append(slash1)
slash.append(slash2)
slash.append(slash3)
slash.append(slash4)

#########################################################################################################################################################

#BackGround##############################################################################################################################################

#Bottom Bricks
x1 = 0
x2 = randint(25,50)
y1 = 600
y2 = y1 + 25
    
for r1 in range(230):
    if y2 >800:
            y2 = 800
     
    for r in range(25):
            if x2 > 800:
                    x2 = 800

            screen.create_rectangle(x1,y1,x2,y2, fill = "#3f4d43", outline = "#536658")
     
            x1 = x2
            randLen = randint(25,50)
            x2 = x1 + randLen

    x1 = 0
    x2 = randint(25,50)
    y1 = y2
    y2 = y2 + 25


#Top Bricks
x1 = 0
x2 = randint (25,50)
y1 = 0
y2 = y1 + 25


for r1 in range(230):
    if y2 >200:
            y2 = 200
     
    for r in range(25):
            if x2 > 800:
                    x2 = 800

            screen.create_rectangle(x1,y1,x2,y2, fill = "#3f4d43", outline = "#536658")
     
            x1 = x2
            randLen = randint(25,50)
            x2 = x1 + randLen

    x1 = 0
    x2 = randint(25,50)
    y1 = y2
    y2 = y2 + 25


#Middle Bricks
x1 = 0
x2 = randint (25,50)
y1 = 200
y2 = y1 + 25


for r1 in range(230):
    if y2 >600:
            y2 = 600
     
    for r in range(25):
            if x2 > 800:
                    x2 = 800

            screen.create_rectangle(x1,y1,x2,y2, fill = "#708275", outline = "#85998b")
     
            x1 = x2
            randLen = randint(25,50)
            x2 = x1 + randLen

    x1 = 0
    x2 = randint(25,50)
    y1 = y2
    y2 = y2 + 25

screen.create_line(0,200,810,200, fill = "#6b756e", width = "10")
screen.create_line(0,600,810,600, fill = "#6b756e", width = "10")

screen.create_rectangle(70, 475, 80, 525, fill = "#705738", outline = "#7d6241")
screen.create_polygon(75, 450, 70, 462.5, 70, 475, 80, 475, 80, 462.5, 75, 450, fill = "#c9a23e", smooth = True)

screen.create_rectangle(395, 475, 405, 525, fill = "#705738", outline = "#7d6241")
screen.create_polygon(400, 450, 395, 462.5, 395, 475, 405, 475, 405, 462.5, 400, 450, fill = "#c9a23e", smooth = True)

screen.create_rectangle(720, 475, 730, 525, fill = "#705738", outline = "#7d6241")
screen.create_polygon(725, 450, 720, 462.5, 720, 475, 730, 475, 730, 462.5, 725, 450, fill = "#c9a23e", smooth = True)

screen.create_polygon(150, 205, 150, 500, 225, 450, 300, 500, 300, 205, 150, 205, fill = "#187041")
screen.create_polygon(500, 205, 500, 500, 575, 450, 650, 500, 650, 205, 500, 205, fill = "#187041")

screen.create_text(225, 352.5, text = "G", font = "Verdana 70")
screen.create_text(575, 352.5, text = "G", font = "Verdana 70")
########################################################################################################################################################

#Blob###########################################################################################################################################
blobs = []

blobxValues = []

blobyValues = []

eyes1 = []

eye1xvalues = []

eye1yvalues = []

eyes2 = []

eye2xvalues = []

eye2yvalues = []


for r in range(5):
    blobs.append(r)
    blobxValues.append(100 + 200*r)
    blobyValues.append(550)
    eyes1.append(0)
    eye1xvalues.append(blobxValues[r] + 30)
    eye1yvalues.append(blobyValues[r] + 10)
    eyes2.append(0)
    eye2xvalues.append(eye1xvalues[r] + 25)
    eye2yvalues.append(eye1yvalues[r])

for b in range(5):
    blobs[b] = screen.create_oval(blobxValues[b], blobyValues[b], blobxValues[b] + 100, blobyValues[b] + 50, fill = "green")
    eyes1[b] = screen.create_oval(eye1xvalues[b], eye1yvalues[b], eye1xvalues[b], eye1yvalues[b], fill = "black", width = "7")
    eyes2[b] = screen.create_oval(eye2xvalues[b], eye2yvalues[b], eye2xvalues[b], eye2yvalues[b], fill = "black", width = "7")
    
j = 0
e1 = 0
e2 = 0
##########################################################################################################################################################

#Animations#####################################################################################################################################

def HackNSlash():
    for r in range(4):
        slashing = screen.create_image(xr,yr,image = slash[r])

        screen.update()
        sleep(0.03)
        screen.delete(slashing)
        
xr = -200
yr = 550
time = 10


for f in range(1500):

    if xr == blobxValues[j]:
        HackNSlash()
        screen.delete(blobs[j],eyes1[e1],eyes2[e2])
        j = j + 1
        e1 = e1 + 1
        e2 = e2 + 1
        
        xC = xr + 35
        yC = yr + 25
        colour = "green"
        maxSize = 4
        
        x = []
        y = []
        r = []
        rSpeeds = []
        angles = []
        startAngles = []
        b = []
        xSizes = []
        ySizes = []
        debris = []
        numDebris = 400

        for debrisNum in range( numDebris ):                                       
     
            x.append( xC )
            y.append( yC )
        
            xSizes.append( randint(1, maxSize) )
            ySizes.append( randint(1, maxSize) )
     
            r.append( 0 ) 
            rSpeeds.append( uniform(1,15) ) 

            newAngle = radians( debrisNum )
            angles.append( newAngle )
            startAngles.append( newAngle )
            b.append(debrisNum*0.0)

            debris.append(0)

    running = screen.create_image(xr,yr,image = run[f % 8])
    xr = xr + 10

    
    if j > 0:
        for i in range( 0, numDebris ):
            debris[i] = screen.create_rectangle( x[i], y[i], x[i] + xSizes[i], y[i] + ySizes[i], fill = colour, outline = colour)
            x[i] = xC + r[i]*cos( angles[i] )
            y[i] = yC - r[i]*sin( angles[i] )
            r[i] = r[i] + rSpeeds[i]
            angles[i] = startAngles[i] + 1.5*sin(0.05*(f-b[i]))

    screen.update()
    sleep(0.03)
   

    if j > 0:
        for i in range(numDebris):
            screen.delete( debris[i] )
            

    screen.delete(running)
##########################################################################################################################################################
            
###Grid lines################################################################################################################################################
spacing = 50

for x in range(0, 1000, spacing):
  screen.create_line(x, 25, x, 1000, fill="white")
  screen.create_text(x, 5, text=str(x), font="Times 9", anchor = N, fill = "white")

for y in range(0, 1000, spacing):
  screen.create_line(25, y, 1000, y, fill="white")
  screen.create_text(5, y, text=str(y), font="Times 9", anchor = W, fill = "white")



