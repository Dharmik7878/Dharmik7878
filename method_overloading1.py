class parent:
    def data(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("The sum of three value is:",a+b+c)
        elif a!=None and b!=None and c==None:
            print("The sum of two value is:",a+b)
        elif a!=None and b==None and c==None:
            print("The square value is:",a*a)

n1=int(input("Enter the value of n1:"))
n2=int(input("Enter the value of n2:"))
n3=int(input("Enter the value of n3:"))

p1=parent()
p1.data(n1)
p1.data(n1,n2)
p1.data(n1,n2,n3)
