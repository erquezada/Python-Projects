import turtle

def draw_flower(t, radius, petals):
    for _ in range(petals):
        t.circle(radius)
        t.left(360 / petals)

# Main script
t = turtle.Turtle()
t.speed("fastest")

draw_flower(t, radius=50, petals=12)

turtle.done()
