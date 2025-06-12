def func():
    a=int(input("Enter the value:"))
    b=int(input("Enter the value:"))
    c=int(input("Enter the value:"))
    d=int(input("Enter the value:"))

    if a>b:
        print("a is greater")
        
    elif b>c:
        print("b is greater")

    elif c>d:
        print("c is greater")

    elif d>a:
        print("d is greater")

    else:
        print("a, b, c and d is sam value:")
def line():
    print("------------------")

line()
func()
line()
