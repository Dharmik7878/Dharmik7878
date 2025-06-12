class demo:
    def __init__(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city
    def show(self):
        print("The public variable is:",self.name)
        print("The privete variable is:",self.age)
        print("The protected variable is:",self.city)

n=input("Enter youe name:")
a=int(input("Enter your age:"))
c=input("Enter your city:")
p1=demo(n,a,c)
p1.show()
