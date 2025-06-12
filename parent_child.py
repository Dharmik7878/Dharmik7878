class parent:
    def getdata(self,name,age):
        self.name=name
        self.age=age
class child(parent):
    def putdata(self):
        print("Your name is:",self.name)
        print("Your age is:",self.age)

n=input("Enter your name:")
a=int(input("Enter your age:"))
p1=child()
p1.getdata(n,a)
p1.putdata()
