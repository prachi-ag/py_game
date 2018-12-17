from random import*
from turtle import*
from base import vector

ant = vector(0,0)
aim = vector(0,40)

def wrap(val):
    return val

def draw():
    ant.move(aim)
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y)
    #aim.rotate(random()*10-500)
    aim.move(-aim*2)
    print(aim)
    clear()
    goto(ant.x,ant.y)
    dot(40)
    if running:
        ontimer(draw,20)

setup(420,420,0,0)
hideturtle()
tracer(False)
up()
running =True
draw()
done()
