import array as myarray
d=myarray.array("i",[10,20,30,40,50])
sum=0
for i in d:
    print(i,end=' ')
    sum=sum+i
print(end='\n')
print("The sum is:",sum)
print("The avg is:",sum/5)
