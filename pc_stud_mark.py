class student:
    def getdata(self,s1,s2,s3,s4,s5):
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
        self.s5=s5
        self.t=0
        self.p=0
class child(student):
    def putdata(self):
        self.t=self.s1+self.s2+self.s3+self.s4+self.s5
        self.p=self.t/5
        print("Total marks is:",self.t)
        print("persetage is:",self.p)

p1=child()
sub1=int(input("Enter subject 1 marks:"))
sub2=int(input("Enter subject 2 marks:"))
sub3=int(input("Enter subject 3 marks:"))
sub4=int(input("Enter subject 4 marks:"))
sub5=int(input("Enter subject 5 marks:"))
p1.getdata(sub1,sub2,sub3,sub4,sub5)
p1.putdata()
