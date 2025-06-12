for r in range(1,6):
    for c in range(1,r+1):
        if (r+c)%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print(end="\n")
        
