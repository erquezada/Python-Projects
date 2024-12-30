import turtle
import random

def draw_line(t, length):
    t.forward(length)
    t.backward(length)

def draw_starburst(t, length, num_lines):
    colors = ["red", "blue", "green", "orange", "purple", "yellow"]
    for _ in range(num_lines):
        t.color(random.choice(colors))
        draw_line(t, length)
        t.right(360 / num_lines)

# Main script
t = turtle.Turtle()
t.speed("fastest")

draw_starburst(t, length=100, num_lines=36)

turtle.done()
