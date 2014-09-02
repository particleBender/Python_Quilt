"""
Anaelisa Aburto
Quilt Project
Quilt Border

"""


import turtle

####################################################################################
#---------------------------- CORNER SQUARE FUNCTION ------------------------------#
####################################################################################

def cornerSquare(r, g, b, sq_size, t):
    t.fill(True)
    t.fillcolor(r,g,b)
    for i in range(0,4):
        t.fd(sq_size*.2)
        t.right(90)
    t.fill(False)

####################################################################################
#------------------------- BLACK BACKGROUND FUNCTION ------------------------------#
####################################################################################
def blackBG(col_num, row_num, sq_size, t):
    t.fill(True)
    t.fillcolor("black")
    for f in range(0,2):
        t.fd(col_num*sq_size+ sq_size*.2)
        t.right(90)
        t.fd(row_num*sq_size + sq_size*.2)
        t.right(90)
    t.fill(False)

####################################################################################
#---------------------------- QUILT BORDERS FUNCTION ------------------------------#
####################################################################################
def quiltBorders(r, g, b, col_num, row_num, sq_size, t):
    t.pu()
    # Setup position of turtle on top left corner
    posX = -(sq_size * col_num ) /2.0 - sq_size*.1
    posY = (sq_size * row_num ) /2.0 + sq_size*.1
    t.setpos(posX, posY)
    t.pd()
    # Draw black background
    blackBG(col_num, row_num, sq_size, t)
    t.pu()
    # Change color value format to RGB 0-255
    turtle.colormode(255)
    # Draw corner squares on top of black background
    for rows in range (0, row_num + 1):
        # Will change value of the BLUE value for each row
        b = b + (150.0/(row_num + 1))
        for cols in range (0, col_num + 1):
            # Setup position for the squares
            t.setpos(posX + cols * sq_size, posY + rows * - sq_size)
            t.pd()
            cornerSquare(r, g, b, sq_size, t)
            # Write the RGB values
            #t.write("%s,%s,%s" % (r, g, b))
            t.pu()

