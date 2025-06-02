st=input("Enter the status:")
g=input("Enetr your gender:")
age=int(input("Enter your age:"))

if st=='m':
    print("are you eligible")
else:
    if g=='m' and age>=30:
        print("are you eligible")
    elif g=='f' and age>=25:
        print("are you eligible")
    else:
        print("you are not eligible")
