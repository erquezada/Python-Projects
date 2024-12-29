import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("sky blue")

# Create the turtle
spiral = turtle.Turtle()
spiral.speed(0)
spiral.width(2)
spiral.hideturtle()

# Define color and movement parameters
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
initial_length = 10  # Initial length of the spiral arm
length_increment = 5  # Incremental increase in length for each step
angle = 30  # Angle of rotation for each step

# Draw the spiral
for i, color in enumerate(colors):
    spiral.color(color)
    spiral.forward(initial_length + i * length_increment)  # Move forward by the calculated length
    spiral.left(angle)  # Turn the turtle by the given angle

# Keep the window open
screen.mainloop()
