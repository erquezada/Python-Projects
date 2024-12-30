import turtle

t = turtle.Turtle()
t.speed(0)

for _ in range(36):
    t.circle(50)
    t.right(10)

# Stem
t.penup()
t.goto(0, -50)
t.pendown()
t.color("green")
t.setheading(270)
t.forward(100)

t.hideturtle()
turtle.done()
