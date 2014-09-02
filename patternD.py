"""
Anaelisa Aburto
001440351
VSFX 705 - Programming Concepts for VFX
Professor Deborah R. Fowler
Quilt Project
Pattern D

"""
import turtle
import math

def patternD(patPosX, patPosY, sq_size, t):
    ##############################################################################################
    #--------------------------------------- SET UP ---------------------------------------------#
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
    #----------------------------------- SQUARES FUNCTION ---------------------------------------#
    ##############################################################################################
    def drawSquare(color, sizeA, sizeB, t):
        t.fillcolor(color)
        t.fill(True)
        for i in range(0,2):
            t.fd(sq_size*sizeA)
            t.right(90)
            t.fd(sq_size*sizeB)
            t.right(90)
        t.fill(False)
    ##############################################################################################
    #------------------------------------- DRAW SQUARES -----------------------------------------#
    ##############################################################################################
    pink = (220,59,97)
    blue = (45,176,201)
    move(-sq_size*.4,sq_size*.4,t)
    drawSquare((212,82,24),.8, .8,t)
    move(-sq_size*.4,sq_size*.26,t)
    drawSquare(pink,.4,.13,t)
    move(-sq_size*.26,sq_size*.26,t)
    drawSquare(blue,.13,.13,t)
    t.right(90)
    move(sq_size*.26,sq_size*.4,t)
    drawSquare(pink,.4,.13,t)
    move(sq_size*.26,sq_size*.26,t)
    drawSquare(blue,.13,.13,t)
    t.right(90)
    move(sq_size*.4,-sq_size*.26,t)
    drawSquare(pink,.4,.13,t)
    move(sq_size*.26,-sq_size*.26,t)
    drawSquare(blue,.13,.13,t)
    t.right(90)
    move(-sq_size*.26,-sq_size*.4,t)
    drawSquare(pink,.4,.13,t)
    move(-sq_size*.26,-sq_size*.26,t)
    drawSquare(blue,.13,.13,t)
    t.right(90)

    ##############################################################################################
    #----------------------------- PURPLE TRIANGLE FUNCTION -------------------------------------#
    ##############################################################################################
    def purpleTriangle(t):
        t.fillcolor(146,37,136)
        t.fill(True)
        t.right(45)
        t.fd(math.sqrt((sq_size*.3)**2 + (sq_size*.3)**2))
        t.right(90)
        t.fd(math.sqrt((sq_size*.3)**2 + (sq_size*.3)**2))
        t.right(135)
        t.fd(sq_size*.6)
        t.fill(False)

    ##############################################################################################
    #------------------------------ DRAW PURPLE TRIANGLES ---------------------------------------#
    ##############################################################################################

    move(-sq_size*.4,sq_size*.3,t)
    purpleTriangle(t)
    move(-sq_size*.3,-sq_size*.4,t)
    purpleTriangle(t)
    move(sq_size*.4,-sq_size*.3,t)
    purpleTriangle(t)
    move(sq_size*.3,sq_size*.4,t)
    purpleTriangle(t)
