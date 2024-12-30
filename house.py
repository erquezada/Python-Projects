import turtle

t = turtle.Turtle()
t.speed(3)

# Base
t.fillcolor("blue")
t.begin_fill()
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

# Roof
t.fillcolor("red")
t.begin_fill()
t.left(45)
for _ in range(3):
    t.forward(70)
    t.left(90)
t.end_fill()

# Door
t.penup()
t.goto(25, -100)
t.pendown()
t.fillcolor("brown")
t.begin_fill()
for _ in range(2):
    t.forward(50)
    t.left(90)
    t.forward(30)
    t.left(90)
t.end_fill()

t.hideturtle()
turtle.done()
