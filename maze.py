from turtle import *
from base import *
from random import random


def draw():
    #clear()
    color("black")  # sets the pen color
    width(5)
    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            if random() > 0.5:
                line(x, y, x + 40, y + 40)
            else:
                line(x, y + 40, x + 40, y)
    update()


def tap(x, y):
    if abs(x) > 198 or abs(y) > 198:
        up()
    else:
        down()
    width(2)
    color('red')
    goto(x, y)
    dot(4)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
draw()
onscreenclick(tap)
done()
