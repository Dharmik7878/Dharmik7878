class maximum:
    def __init__(self,n1,n2):
        self.o=n1;
        self.p=n2;
    def maxi(self):
        if self.o>self.p:
            print("o is maximum..",self.o)
        else:
            print("p is maximum...",self.p)

a=maximum(111,20)
a.maxi()
