no=int(input("Enter the number:"))
sum=0
sum1=0
p=0
n=0
while no!=-111:
    if no>0:
        sum=sum+no
        p=p+1
    else:
        sum1=sum1+no
        n=n+1
    no=int(input("Enter the number:"))
psum=sum/p
nsum=sum1/n
print("Total sum of positive no. ",psum)
print("Total sum of negative no. ",nsum)
