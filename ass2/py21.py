ram=int(input("Enter your age:"))
shyam=int(input("Enter your age:"))
ajay=int(input("Enter your age:"))

if ram<shyam:
    print("ram is youngest")
else:
    if shyam<ajay:
        print("shyam is youngest")
    elif ajay<ram:
        print("ajay is youngest")
    else:
        print("All are same age")
