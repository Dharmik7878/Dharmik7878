no=int(input("Enter the numbr:"))
tmp=no
s=0
t=0
while no>0:
    t=int(no%10)
    s=(s*10)+t
    no=int(no/10)
if tmp==s:
    print("this is pelindrome")
else:
    print("this is not pelindrome")
