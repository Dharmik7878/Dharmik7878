a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))

if a<b:
    if a<c:
        print("a is smallest")
    else:
        print("c is smallest")
else:
    if b<c:
        print("b is smallest")
    else:
        print("c is smallest")
