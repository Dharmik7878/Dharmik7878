import array as myarray
a=myarray.array("i",[10,20,30,40,50])
b=myarray.array("i",[60,70,80,90,100])
c=myarray.array("i",[0,0,0,0,0])
for i in range(0,5):
    c[i]=a[i]+b[i]
print(c)
