import turtle

def draw_rotating_triangles(t, side_length, num_triangles):
    for _ in range(num_triangles):
        for _ in range(3):
            t.forward(side_length)
            t.right(120)
        t.right(360 / num_triangles)

# Main script
t = turtle.Turtle()
t.speed("fastest")

draw_rotating_triangles(t, side_length=100, num_triangles=36)

turtle.done()
