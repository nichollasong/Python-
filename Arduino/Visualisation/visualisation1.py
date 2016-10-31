from graphics import *
from time import *


window = GraphWin("Visualisation", 400, 400)

data= [52, 47, 57, 49, 59, 62, 44, 76, 52, 52, 44, 59, 59, 79, 59, 42, 57, 48, 80, 43, 72, 74, 59, 44, 57, 55, 49, 54, 54]


x=100
y=100
xspeed = 4
yspeed = 5



while True:
    for item in data:
        colour=color_rgb(100,item*2,150)
        ball = circle(Point(x,y), item)
        ball.setFill(color_rgb("green")
        ball.draw(window)
        y=y+yspeed
        x=x+xspeed
        sleep(0.2)
        ball.undraw()
        if y>= 380:
            yspeed=-20
        if y<=10:
            yspeed=20
        if x>=380:
            xspeed=-20
        if x<10:
            xspeed=20



window.getMouse()
