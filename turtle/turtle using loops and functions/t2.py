import turtle
w=turtle.Screen()
w.bgcolor("light blue")
w.title("Turtle")
p=turtle.Turtle()
p.color("red")

def sqrfunc(size):
    for i in range(4):
        p.fd(size)
        p.left(90)
        size = size - 5

sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)
sqrfunc(6)

