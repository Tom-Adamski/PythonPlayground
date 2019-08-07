import turtle
from random import *

MARGIN = 2
SIDE = 20
SPEED = 20

X_MAX = 250
Y_MAX = 250

def square(x,y,side):
    turtle.up()
    turtle.goto(x + MARGIN, y + MARGIN)
    turtle.down()
    turtle.forward(side - 2 * MARGIN)
    turtle.left(90)
    turtle.forward(side - 2 * MARGIN)
    turtle.left(90)
    turtle.forward(side - 2 * MARGIN)
    turtle.left(90)
    turtle.forward(side - 2 * MARGIN)
    turtle.left(90)

def squareGrid(i,j,side):
    square(i * side, j * side, side)


turtle.shape()


distance = 0
r = 1
g = 1
b = 1

##while True:
##    direction = randint(0,2)
##    speed = randint(20,40)
##    if direction == 0:
##        turtle.left(90)
##    elif direction == 2:
##        turtle.right(90)
##    turtle.forward(speed)
##    distance = distance + speed
##    if distance > 100:
##        distance = 0
##        rgb = randint(0,2)
##        if rgb == 0:
##            r = random()
##        elif rgb == 1:
##            g = random()
##        elif rgb == 2:
##            b = random()
##        turtle.pencolor(r,g,b)
##
##    if turtle.xcor() > X_MAX:
##        turtle.up()
##        turtle.setx(- X_MAX)
##        turtle.down()
##    elif turtle.xcor() < (-X_MAX):
##        turtle.up()
##        turtle.setx(X_MAX)
##        turtle.down()
##    elif turtle.ycor() > Y_MAX:
##        turtle.up()
##        turtle.sety(- Y_MAX)
##        turtle.down()
##    elif turtle.ycor() < (-Y_MAX):
##        turtle.up()
##        turtle.sety(Y_MAX)
##        turtle.down()



##while True:
##    angle = randint(0,360)
##    speed = randint(20,100)
##    turtle.left(angle)
##    turtle.forward(speed)
##    distance = distance + speed
##    if distance > 100:
##        distance = 0
##        rgb = randint(0,2)
##        if rgb == 0:
##            r = random()
##        elif rgb == 1:
##            g = random()
##        elif rgb == 2:
##            b = random()
##        turtle.pencolor(r,g,b)
##
##    if turtle.xcor() > X_MAX:
##        turtle.up()
##        turtle.setx(- X_MAX)
##        turtle.down()
##    elif turtle.xcor() < (-X_MAX):
##        turtle.up()
##        turtle.setx(X_MAX)
##        turtle.down()
##    elif turtle.ycor() > Y_MAX:
##        turtle.up()
##        turtle.sety(- Y_MAX)
##        turtle.down()
##    elif turtle.ycor() < (-Y_MAX):
##        turtle.up()
##        turtle.sety(Y_MAX)
##        turtle.down()


while True:
    x = randint(-X_MAX, X_MAX)
    y = randint(-Y_MAX, Y_MAX)
    turtle.goto(x,y)
    rgb = randint(0,2)
    if rgb == 0:
        r = random()
    elif rgb == 1:
        g = random()
    elif rgb == 2:
        b = random()
    turtle.pencolor(r,g,b)
