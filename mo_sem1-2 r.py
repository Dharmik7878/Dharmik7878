class studsem1:
    def getdata(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def rs1(self):
        self.total=self.m1+self.m2+self.m3
        self.per=self.total/3
        print("Your sem1 total is:",self.total)
        print("Your sem2 percemtage is:",self.per)

class studsem2(studsem1):
    def getdata(self,m1,m2,m3,m4,m5,m6):
        super().getdata(m1,m2,m3)
        self.m4=m4
        self.m5=m5
        self.m6=m6
    def rs2(self):
        self.total=self.m4+self.m5+self.m6
        self.per=self.total/3
        print("Your sem2 total is:",self.total)
        print("Your sem2 percentage is:",self.per)

n1=int(input("Enter sub 1 mark:"))
n2=int(input("Enter sub 2 mark:"))
n3=int(input("Enter sub 3 mark:"))
n4=int(input("Enter sub 4 mark:"))
n5=int(input("Enter sub 5 mark:"))
n6=int(input("Enter sub 6 mark:"))

v=studsem2()
v.getdata(n1,n2,n3,n4,n5,n6)
v.rs1()
v.rs2()
