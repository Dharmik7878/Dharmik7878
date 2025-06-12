def calsal(s):
    da=(s*5)/100
    hra=(s*8)/100
    pf=(s*10)/100
    it=(s*12)/100
    ns=(s+da+hra)-(pf+it)
    return ns

sal=int(input("Enter the salary:"))
netsal=calsal(sal)
print("net salary is...",netsal)
