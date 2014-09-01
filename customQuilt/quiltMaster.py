"""
Anaelisa Aburto
Python Quilt
Master File

"""

import turtle
import math

from quiltBorder import *
from patternA import *
from patternB import *
from patternC import *
from patternD import *
from patternE import *


##############################################################################################
#--------------------------------- VARIABLES & SETUP ----------------------------------------#
##############################################################################################

col_num = int(raw_input("Enter number of columns: "))
row_num = int(raw_input("Enter number of rows: "))
margin = int(raw_input("Enter margin size: "))
sq_size = int(raw_input("Enter square size: "))

r = 170
g = 50
b = 50

# Assign name to pen
t = turtle.Pen()
# Assign name to project window
turtle.title("Anaelisa Aburto - My Quilt Project")
# Determines Turtle drawing speed
t.speed(0)


##############################################################################################
#---------------------------- DRAW QUILT FUNCTION -------------------------------------------#
##############################################################################################

def drawQuilt( r, g, b, row_num, col_num, sq_size, margin, t):
    # Setup window size
    turtle.setup( sq_size * col_num + margin + sq_size*.2, sq_size * row_num + margin + sq_size*.2)
    # Move turtle to top left corner
    posX = -(sq_size * col_num ) /2.0 + sq_size/2.0
    posY = (sq_size * row_num ) /2.0 - sq_size/2.0

    # Calls function to draw the quilt border
    quiltBorders(r, g, b, col_num, row_num, sq_size, t)

    # Matrix for quilt
    for rows in range ( row_num ):
        for cols in range( col_num ):
            t.pu()
            # Move turtle over for next row/column position
            patPosX = posX + cols * sq_size
            patPosY = posY + rows * - sq_size
            t.setpos(patPosX, patPosY)
            t.pd()
            if (4-rows + cols) % 5 == 4:
                patternA( patPosX, patPosY, sq_size, t )
            elif (4-rows + cols) % 5 == 3:
                patternB( patPosX, patPosY, sq_size, t )
            elif(4-rows + cols) % 5 == 2:
                patternC( patPosX, patPosY, sq_size, t )
            elif (4-rows + cols) % 5 == 1:
                patternD( patPosX, patPosY, sq_size, t )
            else:
                patternE(patPosX, patPosY, sq_size, t )
            
# Calls function to draw the quilt
drawQuilt( r, g, b, row_num, col_num, sq_size, margin, t)
# Hides the pen
t.hideturtle()
# Click on window to exit
turtle.exitonclick()
