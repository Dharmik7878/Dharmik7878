class perent:
    def getdata(self):
        self.pi=3.14

class child1(perent):
    def circle(self,r):
        self.r=r
        self.cir=self.pi*self.r*self.r
        print("The area of circle is:",self.cir)

class child2(perent):
    def rectangle(self,r):
        self.r=r
        self.rec=2*self.pi*self.r*self.r
        print("The area of rectangle",self.rec)

v=child1()
p=int(input("Enter redius of circle:"))
v.getdata()
v.circle(p)

vv=child2()
pp=int(input("Enter redius of rectangle:"))
vv.getdata()
vv.rectangle(pp)
