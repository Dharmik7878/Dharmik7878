def pri(n1,n2,n3):
    if n1>n2:
        print("n1 is greater")
    elif n2>n3:
        print("n2 is greater")
    elif n3>n1:
        print("n3 is greater")
    else:
        print("both number are sam value")

a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
c=int(input("Enter the vlaue:"))
pri(a,b,c)
