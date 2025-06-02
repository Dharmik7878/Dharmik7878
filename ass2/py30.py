n1=int(input("Enter the first nubmer:"))
n2=int(input("Enter the second number:"))
choise=int(input("Enter your choise:"))
match choise:
    case 1:
        print(n1+n2)
    case 2:
        print(n1-n2)
    case 3:
        print(n1*n2)
    case 4:
        print(n1/n2)
    case _:
        print("invalid input")
