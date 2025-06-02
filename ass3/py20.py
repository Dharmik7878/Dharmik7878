no=int(input("Enter the number:"))
min=no

for i in range(1,11):
    if no>min:
        min=no
    no=int(input("Enter the number:"))
    i=i+1
print("The maximum number is. ",min)
