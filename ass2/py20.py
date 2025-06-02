s1=int(input("Enter the s1 mark:"))
s2=int(input("Enter the s2 mark:"))
s3=int(input("Enter the s3 mark:"))
s4=int(input("Enter the s4 mark:"))
s5=int(input("Enter the s5 mark:"))
per=(s1+s2+s3+s4+s5)/5
print("percentage is:",per)
if per>=60:
    print("A grade")
else:
    if per>50 and per<59:
        print("B grade")
    elif per>40 and per<49:
        print("C grade")
    else:
        print("Fail")
