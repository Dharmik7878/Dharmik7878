(1)
n=int(input("Enter the numner:"))
count=0

for i in range(2,n//2+1):
    if n%i==0:
        count=count+1
        break
if count==0 and n!=1:
    print("%d is a prime:"%n)
else:
    print("%d is not:"%n)

(2){
no=int(input("Enter the number:"))
flag=0

for i in range(2,no):
    if no%i==0:
        flag=1
        break
if flag==0:
    print("no is prime")
else:
    print("no is not prime")
}
