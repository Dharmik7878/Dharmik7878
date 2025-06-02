s=int(input("Enter your salary:"))

if s<=100000:
    print("no tax")
elif s>=100000 and s<150000:
    t=(s*5)/100
    print("tex is ",t)
elif s>=150000 and s<200000:
    t=(s*8)/100
    print("tax is ",t)
elif s>=200000 and s<300000:
    t=(s*10)/100
    print("tax is ",t)
elif s>=300000:
    t=(s*12)/100
    print("tax is ",t)
else:
    print("invalid salary")
