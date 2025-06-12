class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __truediv__(self,other):
        return Vector(self.a / other.a, self.b / other.b)

v1 = Vector(56, 67)
v2 = Vector(8, 6)
print(v1 / v2)
