import turtle
import math

t = turtle.Turtle()
t.speed(0)

# Sun
t.penup()
t.goto(0, -20)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(20)
t.end_fill()

# Planets
def draw_planet(radius, distance, color):
    t.penup()
    t.goto(0, -distance)
    t.pendown()
    t.circle(distance)
    t.penup()
    t.goto(0, -distance + radius)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

draw_planet(10, 50, "blue")
draw_planet(15, 100, "red")

t.hideturtle()
turtle.done()
