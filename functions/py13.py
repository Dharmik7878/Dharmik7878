def max(n1,n2,n3):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
c=int(input("Enter the value:"))

m=max(a,b,c)
print("maximum value is...",m)
