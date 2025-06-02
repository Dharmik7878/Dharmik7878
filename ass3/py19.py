i=1
no=int(input("Enter the number:"))
max=no

while i<10:
    if no>max:
        max=no
    no=int(input("Enter the number:"))
    i=i+1
print("The maximum number is. ",max)
