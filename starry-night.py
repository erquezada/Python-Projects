import turtle
import random

t = turtle.Turtle()
t.hideturtle()
turtle.bgcolor("black")
t.speed(0)

for _ in range(50):
    t.penup()
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    t.pendown()
    t.dot(random.randint(2, 8), "white")

turtle.done()
