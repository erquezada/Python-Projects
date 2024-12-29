import turtle
import colorsys

def draw_rasengan():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Rasengan")

    # Set up the turtle
    rasengan = turtle.Turtle()
    rasengan.hideturtle()
    rasengan.speed(0)  # Fastest speed
    rasengan.tracer(0)  # Turn off animation for faster drawing
    rasengan.width(2)  # Slightly thicker lines for visibility

    # Function to draw a swirl pattern
    def draw_swirl(t, radius, hue_start, hue_end, steps, line_decrement):
        for i in range(steps):
            hue = hue_start + (hue_end - hue_start) * (i / steps)
            color = colorsys.hsv_to_rgb(hue, 1, 1)  # Convert HSV to RGB
            t.pencolor(color)
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.circle(radius, extent=360 / steps)
            radius -= line_decrement  # Decrease the radius for the swirl effect

    # Draw Rasengan layers
    draw_swirl(rasengan, 150, 0.6, 0.65, 100, 1.5)  # Outer swirl
    draw_swirl(rasengan, 120, 0.55, 0.6, 80, 1.2)   # Middle layer
    draw_swirl(rasengan, 90, 0.5, 0.55, 60, 1.0)    # Inner swirl

    rasengan.update()  # Update the screen for final rendering
    turtle.done()

draw_rasengan()
