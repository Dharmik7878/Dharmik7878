no=int(input("Enter the number:"))
sum=0
sum1=0
while no!=-1000:
    if no>0:
        sum=sum+no
    else:
        sum1=sum1+no
    
    no=int(input("Enter the number:"))
print("Total sum of positive no. ",sum)
print("Total sum of negative no. ",sum1)
