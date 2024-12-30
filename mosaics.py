import turtle
import random

t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)

for x in range(-200, 200, 50):
    for y in range(-200, 200, 50):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        t.begin_fill()
        for _ in range(4):
            t.forward(50)
            t.right(90)
        t.end_fill()

t.hideturtle()
turtle.done()
