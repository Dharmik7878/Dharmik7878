class demo:
    def __init__(self):
        self.name="dhamo"
        self.age=21
        self.city="bhavnagar"
    def show(self):
        print("The public variable is:",self.name)
        print("The privete variable is:",self.age)
        print("The protected variable is:",self.city)

p=demo()
p.show()
