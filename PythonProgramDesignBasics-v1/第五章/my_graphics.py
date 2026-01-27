import turtle


def square(x, y, width, color=None):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    if color is not None:
        turtle.fillcolor(color)
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(width)
            turtle.left(90)
        turtle.end_fill()
    else:
        for i in range(4):
            turtle.forward(width)
            turtle.left(90)


def circle(x, y, redius, color=None):
    turtle.penup()
    turtle.goto(x, y - redius)
    turtle.pendown()
    if color is not None:
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(redius)
        turtle.end_fill()
    else:
        turtle.circle(redius)


def line(start_x, start_y, end_x, end_y, color=None):
    turtle.penup()
    turtle.goto(start_x, start_y)
    if color is not None:
        turtle.pencolor(color)
    turtle.pendown()
    turtle.goto(end_x, end_y)
