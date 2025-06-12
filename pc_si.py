class parent:
    def getdata(self,p,r,n):
        self.p=p
        self.r=r
        self.n=n
        self.si=0
class child(parent):
    def putdata(self):
        self.si=self.p*self.r*self.n/100
        print("Simple intrest is:",self.si)

pp=int(input("Enter the amount:"))
nn=int(input("Enter the value:"))
rr=int(input("Enter the rent:"))
p1=child()
p1.getdata(pp,nn,rr)
p1.putdata()
