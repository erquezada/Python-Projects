from turtle import *
from time import sleep, time

def setup_environment():
    """Sets up the turtle environment."""
    speed(0)  # Max speed for smooth drawing
    color('cyan')
    bgcolor('black')
    hideturtle()

def draw_spiral_dynamic(size, decrement):
    """Draws a dynamic spiral pattern."""
    while size > 0:
        right(size)       # Turn the turtle
        forward(size * 3) # Move forward proportional to size
        size -= decrement # Dynamically decrement size for smooth animation

def draw_polygon_dynamic(sides, length, rotation_speed):
    """Draws a polygon dynamically, rotating it in real-time."""
    for _ in range(sides):
        forward(length)
        right(360 / sides)
        sleep(rotation_speed)

def draw_star_dynamic(size, rotation_speed):
    """Draws a star pattern dynamically, animating in real-time."""
    for _ in range(5):
        forward(size)
        right(144)
        sleep(rotation_speed)
        forward(size)
        left(72)

def main():
    """Main function to dynamically animate patterns."""
    setup_environment()
    
    start_time = time()  # Start the timer for dynamic duration
    duration = 15        # Total runtime in seconds
    
    size = 200
    decrement = 2
    while time() - start_time < duration:
        # Alternate between different patterns dynamically
        clear()  # Clear previous drawings for dynamic effect
        draw_spiral_dynamic(size, decrement)
        
        penup()
        goto(-100, 100)
        pendown()
        draw_polygon_dynamic(6, 100, 0.05)
        
        penup()
        goto(100, -100)
        pendown()
        draw_star_dynamic(150, 0.05)
        
        # Dynamically modify size and decrement to change behavior over time
        size = max(50, size - 10)  # Ensure size doesn't become too small
        decrement = max(1, decrement - 0.1)
        
        sleep(1)  # Pause between redraws for real-time effect

    # End the program
    done()

# Run the main function
main()
