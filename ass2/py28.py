c=int(input("Enter the number:"))

match c:
    case 1:
        print("orage")
    case 2:
        print("blue")
    case 3:
        print("black")
    case 4:
        print("red")
    case 5:
        print("gray")
    case _:
        print("invalid input")
