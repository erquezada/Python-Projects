import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

for _ in range(100):
    t.color(random.choice(["red", "blue", "green", "yellow"]))
    t.forward(20)
    t.setheading(random.randint(0, 360))

t.hideturtle()
turtle.done()
