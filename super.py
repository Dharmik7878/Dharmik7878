class perent:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def printvalue1(self):
        print("value of a:",self.a)
        print("value os b:",self.b)

class child(perent):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c=c
    def printvalue2(self):
        print("value os c:",self.c)

x=int(input("Enter the first value:"))
y=int(input("Enter the second value:"))
z=int(input("Enter the third value:"))
v=child(x,y,z)
v.printvalue1()
v.printvalue2()
