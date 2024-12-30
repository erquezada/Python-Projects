import turtle

def draw_star_spiral(t, side_length, increment, num_stars):
    for _ in range(num_stars):
        for _ in range(5):
            t.forward(side_length)
            t.right(144)
        side_length += increment
        t.right(20)

# Main script
t = turtle.Turtle()
t.speed("fastest")

draw_star_spiral(t, side_length=20, increment=5, num_stars=36)

turtle.done()
