import turtle

def draw_spiral_square(t, side_length, increment, num_squares):
    for _ in range(num_squares):
        for _ in range(4):
            t.forward(side_length)
            t.right(90)
        side_length += increment
        t.right(10)  # Slight rotation for the spiral effect

# Main script
t = turtle.Turtle()
t.speed("fastest")  # Maximum speed for faster drawing

draw_spiral_square(t, side_length=20, increment=10, num_squares=36)

turtle.done()
