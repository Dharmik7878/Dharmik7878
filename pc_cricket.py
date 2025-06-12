class cricket:
    def match(self,odi,odiscor,test,testscor):
        self.odi=odi
        self.odiscor=odiscor
        self.test=test
        self.testscor=testscor
        self.tmatch=0
        self.tscor=0
        self.avg=0
class scorbord(cricket):
    def findavg(self):
        self.tmatch=self.odi+self.test
        self.tscor=self.odiscor+self.testscor
        self.avg=self.tscor/self.tmatch
        print("Your average is:",self.avg)

p1=scorbord()
om=int(input("Enter play odi match:"))
oms=int(input("Enter odi match scor is:"))
tm=int(input("Enter play test match:"))
tms=int(input("Enter test match scor is:"))
p1.match(om,oms,tm,tms)
p1.findavg()

