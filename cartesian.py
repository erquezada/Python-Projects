import turtle
import math

def draw_point(x, y, color="red"):
    """Draw a point at the given (x, y) coordinate."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(5, color)

def draw_axes():
    """Draw x and y axes."""
    turtle.speed(0)
    turtle.color("black")
    turtle.penup()
    turtle.goto(-300, 0)
    turtle.pendown()
    turtle.goto(300, 0)  # X-axis
    turtle.penup()
    turtle.goto(0, -300)
    turtle.pendown()
    turtle.goto(0, 300)  # Y-axis
    turtle.penup()

def draw_parabola(a=1, b=0, c=0, color="blue"):
    """Draw a parabola y = ax^2 + bx + c."""
    turtle.penup()
    turtle.color(color)
    for x in range(-300, 301):
        y = a * x**2 / 100 + b * x + c  # Scale the parabola for better visualization
        if -300 <= y <= 300:
            turtle.goto(x, y)
            turtle.pendown()

def draw_stepwise(start, end, step_size, color="green"):
    """Draw a step-wise function."""
    turtle.penup()
    turtle.color(color)
    for x in range(start, end, step_size):
        y = (x // step_size) * 10  # Step function logic
        turtle.goto(x, y)
        turtle.pendown()
        turtle.goto(x + step_size, y)
        turtle.penup()

def main():
    # Set up the turtle screen
    screen = turtle.Screen()
    screen.title("Coordinate System with Functions")
    screen.setup(width=600, height=600)
    screen.setworldcoordinates(-300, -300, 300, 300)  # Set the coordinate system
    screen.tracer(0)  # Disable animation for faster drawing

    # Draw x and y axes
    draw_axes()

    # Plot some points
    points = [(50, 50), (-100, 75), (150, -100), (-200, -200)]
    for x, y in points:
        draw_point(x, y)

    # Draw a parabola
    draw_parabola(a=1, b=0, c=-100)

    # Draw a step-wise function
    draw_stepwise(start=-300, end=300, step_size=50)

    screen.update()  # Update the screen
    screen.mainloop()  # Keep the window open

if __name__ == "__main__":
    main()
