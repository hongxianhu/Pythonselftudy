import turtle

turtle.hideturtle()
turtle.speed(0)
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.forward(100)
for i in range(2):
    turtle.left(90)
    turtle.forward(100)
turtle.end_fill()
turtle.done()