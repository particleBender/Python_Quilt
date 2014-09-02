"""
Anaelisa Aburto
Quilt Project
Pattern E

"""

import turtle
import math

def patternE(patPosX, patPosY, sq_size, t):
    ##############################################################################################
    #----------------------------------------- SETUP --------------------------------------------#
    ##############################################################################################
    # Change color value format to RGB 0-255
    turtle.colormode(255)
    # Pen draw size
    t.width(2)

    ##############################################################################################
    #------------------------------------- MOVE FUNCTION ----------------------------------------#
    ##############################################################################################
    # To move without drawing
    def move(positionX,positionY,t):
        t.pu()
        t.setpos(patPosX+positionX,patPosY+positionY)
        t.pd()

    ##############################################################################################
    #----------------------------- PURPLE TRIANGLE FUNCTION -------------------------------------#
    ##############################################################################################
    def drawTriangle(color,size,t):
        t.fillcolor(color)
        t.fill(True)
        t.right(45)
        t.fd(math.sqrt((sq_size*size)**2 + (sq_size*size)**2))
        t.right(90)
        t.fd(math.sqrt((sq_size*size)**2 + (sq_size*size)**2))
        t.right(135)
        t.fd(sq_size*size*2)
        t.fill(False)

    ##############################################################################################
    #------------------------------ DRAW PURPLE TRIANGLES ---------------------------------------#
    ##############################################################################################
    # Draw big triangles
    move(-sq_size*.4,sq_size*.4,t)
    drawTriangle((214,87,80),.4,t)
    move(-sq_size*.4,-sq_size*.4,t)
    drawTriangle((136,45,105),.4,t)
    move(sq_size*.4,-sq_size*.4,t)
    drawTriangle((214,87,80),.4,t)
    move(sq_size*.4,sq_size*.4,t)
    drawTriangle((136,45,105),.4,t)
    # Draw small triangles
    move(-sq_size*.4,sq_size*.2,t)
    drawTriangle((128,195,204),.2,t)
    move(-sq_size*.2,-sq_size*.4,t)
    drawTriangle((108,108,48),.2,t)
    move(sq_size*.4,-sq_size*.2,t)
    drawTriangle((128,195,204),.2,t)
    move(sq_size*.2,sq_size*.4,t)
    drawTriangle((108,108,48),.2,t)

    ##############################################################################################
    #----------------------------- BLUE/GREEN SQUARE FUNCTION -----------------------------------#
    ##############################################################################################
    def yellowblueTriangle(t):
        # Makes a yellow square
        t.fillcolor(233,175,71)
        t.fill(True)
        for i in range(0,4):
            t.fd(sq_size*.2)
            t.right(90)
        t.fill(False)
        # Makes a blue triangle on top of the yellow square
        t.fillcolor(128,195,204)
        t.fill(True)
        t.fd(sq_size*.2)
        t.right(135)
        t.fd(math.sqrt((sq_size*.2)**2 + (sq_size*.2)**2))
        t.right(135)
        t.fd(sq_size*.2)
        t.fill(False)

    ##############################################################################################
    #------------------------------- DRAW YELLOW/BLUE SQUARE ------------------------------------#
    ##############################################################################################

    move(-sq_size*.4,sq_size*.4,t)
    yellowblueTriangle(t)
    move(-sq_size*.4,-sq_size*.4,t)
    yellowblueTriangle(t)
    move(sq_size*.4,-sq_size*.4,t)
    yellowblueTriangle(t)
    move(sq_size*.4,sq_size*.4,t)
    yellowblueTriangle(t)
