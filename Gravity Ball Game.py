##########################
#        ZigZaggah       #
##########################
from tkinter import *
from math import *
from time import *
from random import *

root = Tk()
s = Canvas( root, width=1000, height=1000, background="white" )
s.pack()
#Initial Values#########################################
def setInitialValues():
    global score, time, frameNum
    global xBall, yBall, qPressed, ySpeed
    global i, ball
    global Onumber, Ox, Oy, OxSpeed, oSpace, OxSpeed, ObstacleDrawings, rate

    ySpeed = 7
    rate = 50

    qPressed = False

    ball = []
    xBall = 300
    yBall = 500

    ObstacleDrawings = []
    Ox = []
    Oy = []
    OxSpeed = 10
    oSpace = 25
    frameNum = 100
    Onumber = 100
    
    for i in range(100):
        Ox.append( randint(1000,10000 ))
        Oy.append( randint(0,1000 ))
        
    for i in range(100):
        ObstacleDrawings.append(0)

    
########################################################

#Input Handling#########################################
def mouseClickHandler( event ):
    global ySpeed
    ySpeed = ySpeed*-1

def mouseReleaseHandler( event ):
    global ySpeed
    ySpeed = ySpeed

def keyDownHandler( event ):
	global qPressed

	if event.keysym == "q" or event.keysym == "Q":
		qPressed = True
#########################################################

#Main Sprite Animation###################################
def drawObject():
    global ball

    ball = s.create_oval(xBall - 10 , yBall - 10, xBall + 10, yBall + 10, outline = "black", fill = "black")

def updateObject():
    global yBall, ySpeed
    yBall = yBall + ySpeed
#########################################################

#Creation/Updating of Obstacles##########################

def drawObstacles():
    global i, Ox, Oy, xSpeed, Onumber, oSpace, OxSpeed, ObstacleDrawings
    for i in range(100):
        ObstacleDrawings[i] = s.create_oval(Ox[i] - oSpace, Oy[i] - oSpace, Ox[i] + oSpace, Oy[i] + oSpace, outline = "black", fill = "black")

def updateObstacles():
    global Ox
    for i in range(100):
        Ox[i] = Ox[i] - OxSpeed

def oSpeedUp():
    global OxSpeed
    OxSpeed = frameNum / rate


            
        
#########################################################

#Collisions##############################################
#def checkForCollisions():
    
#Functionality###########################################   
def endGame():
    root.destroy
    
def runGame():  
    global i, frameNum
    setInitialValues()
    
    while qPressed == False:   #Repeats 100’s of times per second, whether the player is doing anything or notdrawObjects()  #This should draw only the current frame
        drawObject()
        drawObstacles()
    
        s.update()
        sleep(0.03)
        s.delete(ball)

        for i in range(100):
            s.delete(ObstacleDrawings[i])

        updateObject()
        updateObstacles()
        #checkForCollisions()
        frameNum = frameNum + 1
        oSpeedUp()
        

    endGame()
    print(ObstacleDrawings)
##########################################################

    
#STARTS THE GAME BY PASSING CONTROL TO THE PROCEDURE runGame() 500 MILLISECONDS AFTER PUSHING F5
root.after(0, runGame)

#BINDINGS 
s.bind("<Button-1>", mouseClickHandler) #Makes the procedure named mouseClickHandler() get called every time the user clicks the left mouse button.
s.bind("<ButtonRelease-1>", mouseReleaseHandler) 
s.bind( "<Key>", keyDownHandler)

s.pack()
s.focus_set()
root.mainloop()




