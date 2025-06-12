class simin:
    def __init__(self,n1,n2,n3):
        self.p=n1;
        self.r=n2;
        self.n=n3;
        self.si=0;
    def sin(self):
        self.si=(self.p*self.r*self.n)/100
        print("Your intrest is:",self.si)

a=simin(10000,5,2)
a.sin()
