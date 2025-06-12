def add(x,y):
    print("the addition is...",x+y)

def sub(p,q):
    print("the subtraction is...",p+q)

def mul(a,b):
    print("the multiplication is...",a*b)

def div(m,n):
    print("the division is...",m/n)

def line():
    print("-------------------------------------")

line()
n1=int(input("Enter the first value:"))
n2=int(input("Enter the second value:"))
line()
add(n1,n2)
line()
sub(n1,n2)
line()
mul(n1,n2)
line()
div(n1,n2)
line()
