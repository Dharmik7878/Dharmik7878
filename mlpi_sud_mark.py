class stud:
    def getmark(self,s1,s2,s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3
class result(stud):
    def cal(self):
        self.t=self.s1+self.s2+self.s3
        self.p=self.t/3
class d(result):
    def display(self):
        print("Total marks is:",self.t)
        print("Persentage is:",self.p)
class gread(d):
    def grd1(self):
        if self.p>70:
            print("A")
        elif self.p<70 and self.p>60:
            print("B")
        elif self.p<60 and self.p>50:
            print("c")
        elif self.p<50 and self.p>40:
            print("d")
        else:
            print("fail")

p1=gread()
sub1=int(input("Enter a sub 1 marks:"))
sub2=int(input("Enter a sub 2 marks:"))
sub3=int(input("Enter a sub 3 marks:"))
p1.getmark(sub1,sub2,sub3)
p1.cal()
p1.display()
p1.grd1()










