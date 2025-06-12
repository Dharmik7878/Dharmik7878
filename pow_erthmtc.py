class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return "Vector (%d, %d)" % (self.a, self.b)

    def __pow__(self,other):
        return Vector(self.a ** other.a, self.b ** other.b)

v1 = Vector(6, 3)
v2 = Vector(3, 6)
print("The answer is:",v1 ** v2)
