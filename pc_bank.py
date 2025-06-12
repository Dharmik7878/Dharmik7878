class bank:
    def getdata(self,cr,db):
        self.cr=cr
        self.db=db
        self.bal=0
class child(bank):
    def putdata(self):
        print("credited amount:",self.bal+self.cr)
        print("debited amount:",self.bal-self.db)
        print("curent balance is:",self.bal+self.cr-self.db)
        

p1=child()
credit=int(input("Enter your credit amount:"))
debit=int(input("Enter your debit amount:"))
p1.getdata(credit,debit)
p1.putdata()
