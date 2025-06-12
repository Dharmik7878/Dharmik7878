import turtle
clr = ["orange", "white", "green"]
mypen = turtle.pen()
mypen=turtle.Turtle()
mypen.speed(100)
turtle.bgcolor("black")

for x in range(365):
    mypen.pencolor(clr[x % 3])
    mypen.width(x/100 + 1)
    mypen.forward(x)
    mypen.left(90)
