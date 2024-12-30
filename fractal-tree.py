import turtle

t = turtle.Turtle()
t.speed(0)

def draw_tree(length):
    if length < 10:
        return
    t.forward(length)
    t.left(30)
    draw_tree(length - 10)
    t.right(60)
    draw_tree(length - 10)
    t.left(30)
    t.backward(length)

t.left(90)
draw_tree(100)
t.hideturtle()
turtle.done()
