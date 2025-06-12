class cal:
    def __init__(self,n1,n2,n3):
        self.a=n1;
        self.b=n2;
        self.c=n3;
        self.ans=0;
    def sum(self):
        self.ans=self.a+self.b+self.c;
        print("The sum is:",self.ans)

c1=cal(10,20,30)
c1.sum()

c2=cal(70,45,76)
c2.sum()
