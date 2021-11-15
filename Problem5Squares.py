#Jaden
#11/13/2021
# This code will create multiple squares inside of itself.

import turtle
def drawSquare (t,sz):
        """Get turtle t to draw a squae of sz side"""
        for i in range(4):
            t.forward(sz)
            t.left(90)
            t.hideturtle()

wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")


size = 20


for i in range(5):
        drawSquare(alex, size)
        size = size + 20
        alex.penup()
        alex.goto(alex.pos() + (-10, -10))
        alex.pendown()

wn.exitonclick()
