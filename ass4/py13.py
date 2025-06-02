no=int(input("Enter the number:"))
a=1
b=0

for i in range(1,no+1):
    print(a,end=" ")
    c=a+b
    b=a
    a=c
