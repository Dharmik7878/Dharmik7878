s=int(input("Enter the salary:"))
g=input("Enter your gander")

if g=="female" and s>=5000:
    b=(s*15)/100
    print("bonus is ",b)
elif g=="male" and s>=5000:
    b=(s*10)/100
    print("bonus is ",b)
else:
    print("invalid salary")
