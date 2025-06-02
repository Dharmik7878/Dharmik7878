p=int(input("Enter the principal:"))
n=int(input("Ennter the year:"))
if n<5:
    r=5
    ans=(p*r*n)/100
else:
    r=10
    ans=(p*r*n)/100
print("the ans is:",ans)
