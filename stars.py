import turtle

def draw_star(t, side_length):
    # Draw a regular star with 7 sides
    for _ in range(5):
        t.forward(side_length)
        t.right(144)

def draw_pattern(t, side_length, number_of_stars):
    # Draw a pattern of stars using the draw_star function
    for _ in range(number_of_stars):
        draw_star(t, side_length)
        t.penup()  # Lift the pen to move without drawing
        t.forward(side_length * 3)  # Move to the next position
        t.pendown()  # Lower the pen to draw

# Main script
t = turtle.Turtle()
t.speed("fast")  # Set turtle speed to fast
side_length = 100
number_of_stars = 5

draw_pattern(t, side_length, number_of_stars)

turtle.done()
