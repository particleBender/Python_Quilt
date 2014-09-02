"""
Anaelisa Aburto
001440351
VSFX 705 - Programming Concepts for VFX
Professor Deborah R. Fowler
Quilt Project
Pattern B

"""

import turtle
import math

def patternB(patPosX, patPosY, sq_size, t):
    ##############################################################################################
    #----------------------------------------- SETUP --------------------------------------------#
    ##############################################################################################
    # Change color value format to RGB 0-255
    turtle.colormode(255)
    # Pen draw size
    t.width(2)

    ##############################################################################################
    #--------------------------------- BLUE SQUARE FUNCTION -------------------------------------#
    ##############################################################################################
    def blueSquare(size):
        t.fillcolor(0,127,105)
        t.fill(True)
        for i in range(0,4):
            t.fd(sq_size*size)
            t.right(90)
        t.fill(False)

    ##############################################################################################
    #------------------------------- DRAW BIG BLUE SQUARE ---------------------------------------#
    ##############################################################################################
    t.pu()
    t.setpos(patPosX-sq_size*.4,patPosY+sq_size*.4)
    t.pd()
    blueSquare(.8)

    ##############################################################################################
    #--------------------------------- DRAW PINK DIAMOND ----------------------------------------#
    ##############################################################################################
    t.fillcolor(237,77,96)
    t.pu()
    t.setpos(patPosX,patPosY-sq_size*.4)
    t.pd()
    t.fill(True)
    t.circle(sq_size*.4, 360, 4)
    t.fill(False)

    ##############################################################################################
    #--------------------------------- DRAW SMALL BLUE SQUARE -----------------------------------#
    ##############################################################################################
    t.pu()
    t.setpos(patPosX-sq_size*.2,patPosY+sq_size*.2)
    t.pd()
    blueSquare(.4)

    ##############################################################################################
    #--------------------------------- DRAW ORANGE DIAMOND --------------------------------------#
    ##############################################################################################
    t.fillcolor(228,88,48)
    t.pu()
    t.setpos(patPosX,patPosY-sq_size*.2)
    t.pd()
    t.fill(True)
    t.circle(sq_size*.2, 360, 4)
    t.fill(False)

    ##############################################################################################
    #--------------------------- ORANGE/PURPLE SQUARE FUNCTION -----------------------------------#
    ##############################################################################################
    def orangeTriangle(t):
        # Makes a purple square
        t.fillcolor(90,36,124)
        t.fill(True)
        for i in range(0,4):
            t.fd(sq_size*.2)
            t.right(90)
        t.fill(False)
        # Makes a orange triangle on top of the purple square
        t.fillcolor(228,88,48)
        t.fill(True)
        t.fd(sq_size*.2)
        t.right(135)
        t.fd(math.sqrt((sq_size*.2)**2 + (sq_size*.2)**2))
        t.right(135)
        t.fd(sq_size*.2)
        t.fill(False)

    ##############################################################################################
    #----------------------------- DRAW ORANGE/PURPLE SQUARE ------------------------------------#
    ##############################################################################################
    t.pu()
    t.setpos(patPosX-sq_size*.4,patPosY+sq_size*.4)
    t.pd()
    orangeTriangle(t)
    t.setpos(patPosX-sq_size*.4,patPosY-sq_size*.4)
    orangeTriangle(t)
    t.setpos(patPosX+sq_size*.4,patPosY-sq_size*.4)
    orangeTriangle(t)
    t.setpos(patPosX+sq_size*.4,patPosY+sq_size*.4)
    orangeTriangle(t)