import turtle

def draw_hexagon(t, side_length):
    for _ in range(6):
        t.forward(side_length)
        t.right(60)

def draw_snowflake(t, side_length, num_hexagons):
    for _ in range(num_hexagons):
        draw_hexagon(t, side_length)
        t.right(360 / num_hexagons)

# Main script
t = turtle.Turtle()
t.speed("fastest")

draw_snowflake(t, side_length=50, num_hexagons=12)

turtle.done()
