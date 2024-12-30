import turtle
import random

turtle.speed(0)
turtle.bgcolor("white")

# Draw track
for i in range(-200, 201, 100):
    turtle.penup()
    turtle.goto(-300, i)
    turtle.pendown()
    turtle.forward(600)

# Racers
colors = ["red", "blue", "green"]
racers = [turtle.Turtle() for _ in range(3)]

for i, racer in enumerate(racers):
    racer.color(colors[i])
    racer.shape("turtle")
    racer.penup()
    racer.goto(-300, 150 - i * 100)

# Race
finished = False
while not finished:
    for racer in racers:
        racer.forward(random.randint(1, 5))
        if racer.xcor() > 300:
            finished = True
            print(f"{racer.color()[0]} turtle wins!")
            break

turtle.done()
