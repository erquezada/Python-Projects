import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

# Setup turtle
t = turtle.Turtle()
t.pencolor("white")
t.speed(0)  # Fastest speed
t.hideturtle()

# Initial parameters
a = 0
b = 0

# Start drawing
t.penup()
t.goto(0, 200)
t.pendown()

# Draw pattern
while b < 210:  # Simplified condition
    t.forward(a)
    t.right(b)
    a += 3
    b += 1

# Close turtle graphics window on click
screen.mainloop()
