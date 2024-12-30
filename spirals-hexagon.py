import turtle

t = turtle.Turtle()
t.speed(0)
colors = ["red", "blue", "green", "yellow"]

for i in range(100):
    t.color(colors[i % 4])
    t.forward(i * 2)
    t.left(59)

t.hideturtle()
turtle.done()
