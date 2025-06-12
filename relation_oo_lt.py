class parent:
    def __init__(self,a):
        self.a=a

    def __lt__(self,other):
        if self.a < other.a:
            return self.a
        else:
            return other.a

n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))

p1 = parent(n1)
p2 = parent(n2)

p3 = p1 < p2
print("Your value is:",p3)
