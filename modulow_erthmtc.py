class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __mod__(self,other):
        return Vector(self.a % other.a, self.b % other.b)

v1 = Vector(55, 55)
v2 = Vector(7, 8)
print("the answer is:",v1 % v2)
