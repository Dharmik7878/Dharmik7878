g=input("Enter your gender:")
s=int(input("Enter year of service:"))
q=input("Enter your qualification")

if g=="male" or g=="Male" or g=="MALE" and s>=10 and q=="pg":
    print("Your salary is 15000")
    
elif g=="male" or g=="Male" or g=="MALE" and s<10 and q=="pg":
    print("your salary is 10000")
    
elif g=="male" or g=="Male" or g=="MALE" and s>=10 and q=="g":
    print("Your salary is 10000")
    
elif g=="male" or g=="Male" or g=="MALE" and s<10 and q=="g":
    print("Your salary is 7000")
    
elif g=="female" or g=="Female" or g=="FEMALE" and s>=10 and q=="pg":
    print("Your salary is 12000")
    
elif g=="female" or g=="Female" or g=="FEMALE" and s<10 and q=="pg":
    print("Your salary is 7000")
    
elif g=="female" or g=="Female" or g=="FEMALE" and s>=10 and q=="g":
    print("Your salary is 10000")
    
elif g=="female" or g=="Female" or g=="FEMALE" and s<10 and q=="g":
    print("Your salary is 6500")

else:
    print("invalid input")
    
