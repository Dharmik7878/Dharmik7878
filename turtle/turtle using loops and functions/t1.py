import turtle
w=turtle.Screen()
w.bgcolor("light blue")
w.title("Turtle")
p=turtle.Turtle()
p.color("red")

def sqrfunc(size):
    for i in range(10):
        p.circle(size)
        #p.left(90)
        size = size + 5

sqrfunc(20)
