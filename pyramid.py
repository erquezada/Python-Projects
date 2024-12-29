import turtle

t = turtle.Turtle()
t.speed(9)
side =0 

while side < 201:
    t.forward(side)
    t.right(90)
    side += 2

for i in range(201):
    t.backward(-side)
    t.right(90)
    side -= 1

t.hideturtle()
turtle.done()