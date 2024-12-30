import turtle
import colorsys

def draw_rainbow_spiral(t, size, num_loops):
    hue = 0
    for _ in range(num_loops):
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        t.color(color)
        t.forward(size)
        t.right(45)
        hue += 0.01  # Increment hue for the rainbow effect

# Main script
t = turtle.Turtle()
t.speed("fastest")
turtle.colormode(255)  # Allows RGB values

draw_rainbow_spiral(t, size=5, num_loops=100)

turtle.done()
