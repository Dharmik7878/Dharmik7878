class studsem1:
    def getdata(self,m1,m2,m3,m4):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.m4=m4
    def rs1(self):
        self.total=self.m1+self.m2+self.m3+self.m4
        self.per=self.total/4
        print("Your sem1 total is:",self.total)
        print("Your sem2 percemtage is:",self.per)

class studsem2(studsem1):
    def getdata(self,m1,m2,m3,m4,m5,m6,m7,m8):
        super().getdata(m1,m2,m3,m4)
        self.m5=m5
        self.m6=m6
        self.m7=m7
        self.m8=m8
    def rs2(self):
        self.total=self.m5+self.m6+self.m7+self.m8
        self.per=self.total*/4
        print("Your sem2 total is:",self.total)
        print("Your sem2 percentage is:",self.per)

class studsem3(studsem2):
    def getdata(self,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12):
        super().getdata(m1,m2,m3,m4,m5,m6,m7,m8)
        self.m9=m9
        self.m10=m10
        self.m11=m11
        self.m12=m12
    def rs3(self):
        self.total=self.m9+self.m10+self.m11+self.m12
        self.per=self.total/4
        print("Your sem2 total is:",self.total)
        print("Your sem2 percentage is:",self.per)

class studsem4(studsem3):
    def getdata(self,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12,m13,m14,m15,m16):
        super().getdata(m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,m12)
        self.m13=m13
        self.m14=m14
        self.m15=m15
        self.m16=16
    def rs4(self):
        self.total=self.m13+self.m14+self.m15+self.m16
        self.per=self.total/4
        print("Your sem2 total is:",self.total)
        print("Your sem2 percentage is:",self.per)

n1=int(input("Enter sub 1 mark:"))
n2=int(input("Enter sub 2 mark:"))
n3=int(input("Enter sub 3 mark:"))
n4=int(input("Enter sub 4 mark:"))
n5=int(input("Enter sub 5 mark:"))
n6=int(input("Enter sub 6 mark:"))
n7=int(input("Enter sub 7 mark:"))
n8=int(input("Enter sub 8 mark:"))
n9=int(input("Enter sub 9 mark:"))
n10=int(input("Enter sub 10 mark:"))
n11=int(input("Enter sub 11 mark:"))
n12=int(input("Enter sub 12 mark:"))
n13=int(input("Enter sub 13 mark:"))
n14=int(input("Enter sub 14 mark:"))
n15=int(input("Enter sub 15 mark:"))
n16=int(input("Enter sub 16 mark:"))

v=studsem4()
v.getdata(n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16)
v.rs1()
v.rs2()
v.rs3()
v.rs4()
