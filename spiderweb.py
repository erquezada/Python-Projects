import turtle

def draw_spider_web(t, rings, spokes, radius):
    angle = 360 / spokes
    for _ in range(spokes):
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.forward(radius)
        t.right(angle)
    
    for r in range(1, rings + 1):
        t.penup()
        t.goto(0, -radius * r / rings)
        t.pendown()
        t.circle(radius * r / rings)

# Main script
t = turtle.Turtle()
t.speed("fastest")

draw_spider_web(t, rings=5, spokes=12, radius=200)

turtle.done()
