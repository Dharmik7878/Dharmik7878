class myclass:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
    def myfun(self):
        print("Your name is:",self.name)
        print("Your age is:",self.age)

nam=input("Enter your name:")
varas=int(input("Enter your age:"))
p1=myclass(nam,varas)
p1.myfun()
