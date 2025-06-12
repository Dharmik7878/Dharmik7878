fp=open("triengle.txt","w")
for r in range(1,6):
    for c in range(1,r+1):
        fp.write("*")
    fp.write("\n")

fp.close()

