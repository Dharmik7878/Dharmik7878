bs=int(input("Enter your salary:"))
hra=250
if bs>=5000:
    da=(bs*5)/100
else:
    da=(bs*7)/100
gs=bs+hra+da
print("gross salary is...",gs)
