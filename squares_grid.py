import turtle

def draw_square(t, side_length):
    for _ in range(4):
        t.forward(side_length)
        t.right(90)

def draw_grid(t, rows, cols, side_length):
    for i in range(rows):
        for j in range(cols):
            draw_square(t, side_length)
            t.penup()
            t.forward(side_length)
            t.pendown()
        t.penup()
        t.backward(side_length * cols)
        t.right(90)
        t.forward(side_length)
        t.left(90)
        t.pendown()

# Main script
t = turtle.Turtle()
t.speed("fastest")

draw_grid(t, rows=5, cols=5, side_length=50)

turtle.done()
