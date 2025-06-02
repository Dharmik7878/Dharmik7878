no=int(input("Enter the number:"))

while no!=-101:
    i=1
    fact=1
    while i<=no:
        fact=fact*i
        i=i+1
    print("The factorial is. ",fact)
    no=int(input("Enter the number:"))
