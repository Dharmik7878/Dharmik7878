class bca:
    def sem(self,sem1,sem2,sem3,sem4):
        self.sem1=sem1
        self.sem2=sem2
        self.sem3=sem3
        self.sem4=sem4
        self.total=0
        self.pr=0
class child(bca):
    def avg(self):
        self.total=self.sem1+self.sem2+self.sem3+self.sem4
        self.avg=self.total*100/1520
        print("Your total marks is:",self.total)
        print("Your avg is:",self.avg)

p1=child()
s1=int(input("Enter the sem1 marks:"))
s2=int(input("Enter the sem2 marks:"))
s3=int(input("Enter the sem3 marks:"))
s4=int(input("Enter the sem4 marks:"))
p1.sem(s1,s2,s3,s4)
p1.avg()
