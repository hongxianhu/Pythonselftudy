import turtle
import my_graphics as mg
import random


def main():
    turtle.hideturtle()
    turtle.speed(0)
    # test1()
    test2()
    turtle.done()


def test1():
    x = 0
    y = 0
    z = 1
    for i in range(0, 81, 20):
        for j in range(0, 81, 20):
            if z % 2 != 0:
                mg.square(x + j, y + i, 20, color="black")
            else:
                mg.square(x + j, y + i, 20, color="white")
            z += 1


def test2():
    mg.square(0, 0, 300, color="black")
    test2_1()
    test2_2()


def test2_1():
    for i in range(20):
        turtle.pencolor("white")
        turtle.pensize(0)
        turtle.penup()
        turtle.goto(random.randint(0, 300), random.randint(100, 300))
        turtle.pendown()
        turtle.dot()


def test2_2():
    turtle.fillcolor("gray")
    turtle.begin_fill()
    mg.line(0, 0, 0, 100)
    mg.line(0, 100, 300, 100)
    mg.line(300, 100, 300, 0)
    mg.line(300, 0, 0, 0)
    turtle.end_fill()

def test2_3():
    pass

def test2_4():
    pass

def test3():
    pass


if __name__ == "__main__":
    main()
