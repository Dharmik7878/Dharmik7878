class demo:
    def __init__(self):
        self.name="dhamo"
        self.__age=21
        self._city="Bhavnagar"
    def show(self):
        print("The public variable is:",self.name)
        print("The privete variable is:",self.__age)
        print("The protected variable is:",self._city)

p=demo()
p.show()
