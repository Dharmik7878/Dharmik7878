class bank:
    def __init__(self):
        self.blc=0
        self.c=0
        self.d=0
    def crdt(self,cr):
        self.c=cr
        print("credit amount is:",self.blc+self.c)
    def dbt(self,db):
        self.d=db
        print("debited amount is:",self.blc+self.c-self.d)

p1=bank()
print("curent balance is:",p1.blc)
#print("credit balance is:",p1.c)
#print("debit balance is:",p1.d)
crd=int(input("Enter credit amount:"))
p1.crdt(crd)
dbtt=int(input("Enter debit amount:"))
p1.dbt(dbtt)
#print("curent balance is:",p1.c-p1.d)
print("Thank you")
