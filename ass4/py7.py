no=int(input("Enter the number:"))
for i in range(1,no+1):
    ans=1
    for j in range(1,i+1):
        ans=ans*j
    print(ans,end=" ")
