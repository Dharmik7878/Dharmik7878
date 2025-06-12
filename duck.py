class Duck:
    def sound(self):
        return "Queck,queck"

class Anotherbird:
    def sound(self):
        return "T'm similar to a duck!"

def makeSound(D):
    print(D.sound())

duck=Duck()
anotherbird=Anotherbird()
makeSound(duck)
makeSound(anotherbird)
