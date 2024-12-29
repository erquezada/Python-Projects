from turtle import *

# Set up the turtle environment
speed(0)  # Maximize speed for faster drawing
color('cyan')
bgcolor('black')

# Initializing the size variable
size = 200

# Drawing loop
while size > 0:
    right(size)       # Turn the turtle
    forward(size * 3) # Move forward proportional to size
    size -= 1         # Decrement size to change the shape dynamically

# End the program properly
done()
