class demo:
    def data(self):
        print("only self method call:")

    def data(self,n1):
        self.n1=n1
        print("The squer is:",self.n1 * self.n1)

    def data(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print("The sum is:",self.n1 + self.n2)
        
    def data(self,n1,n2,n3):
        self.n1=n1
        self.n2=n2
        self.n3=n3
        print("The sum or sub is:",self.n1 + self.n2 - self.n3)

no1=int(input("Enter no1 value:"))
no2=int(input("Enter no2 value:"))
no3=int(input("Enter no3 value:"))

d1=demo()
d1.data(no1)
d1.data(no1,no2)
d1.data(no1,no2,no3)
