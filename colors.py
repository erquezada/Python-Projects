import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create the turtle
artist = turtle.Turtle()
artist.speed(0)
artist.hideturtle()

# Color palette
colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# Draw a spiral pattern
for angle in range(360):
    artist.color(colors[angle % len(colors)])
    artist.forward(angle * 0.5)
    artist.right(59)

# Keep the window open
screen.mainloop()
