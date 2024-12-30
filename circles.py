import turtle

def draw_concentric_circles(t, start_radius, increment, num_circles):
    for _ in range(num_circles):
        t.circle(start_radius)
        start_radius += increment

# Main script
t = turtle.Turtle()
t.speed("fastest")

draw_concentric_circles(t, start_radius=20, increment=10, num_circles=10)

turtle.done()
