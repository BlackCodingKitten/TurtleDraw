import turtle

turtle.bgcolor('black')
turtle.pensize('4')

def curve():
    for i in range(200):
        turtle.speed(1)
        turtle.right(1)
        turtle.forward(1)

turtle.speed(1)
turtle.color('red', 'red')

turtle.begin_fill()
turtle.left(140)
turtle.forward(111.65)

curve()
turtle.left(120)
curve()
turtle.forward(111.65)
turtle.end_fill()
turtle.hideturtle()
