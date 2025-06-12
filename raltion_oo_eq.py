class parent:
    def __init__(self,a):
        self.a=a

    def __eq__(self,other):
        if self.a == other.a:
            print("true")
        else:
            print("false")

n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))

p1 = parent(n1)
p2 = parent(n2)

p3=p1 == p2
