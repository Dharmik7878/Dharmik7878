class gperent:
    def getdata(self,rollno,name):
        self.rollno=rollno
        self.name=name
        
class perent(gperent):
    def mark(self,s1,s2,s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3

class sport:
    def renk(self,rn):
        self.rn=rn

class child(perent,sport):
    def result(self):
        self.total=self.s1+self.s2+self.s3
        self.per=self.total/3
        print("Your roll no:",self.rollno)
        print("Your name is:",self.name)
        print("YOur total marks is:",self.total)
        print("Your percentage is:",self.per)

v=child()
r=int(input("Enter your no:"))
n=input("Enter your name:")
sub1=int(input("Enter s1 mark:"))
sub2=int(input("Enter s2 mark:"))
sub3=int(input("Enter s3 mark:"))
renk=int(input("Enter your renk:"))
v.getdata(r,n)
v.mark(sub1,sub2,sub3)
v.result()
v.renk(renk)
