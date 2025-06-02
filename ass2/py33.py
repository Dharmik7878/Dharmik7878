no=int(input("Enter the notes:"))
h=(int)(no/100)
p=(int)(no-(h*100))/5
t=(int)(no-((h*100)+(p*50)))/20
te=(int)(no-((h*100)+(p*50)+(t*20)))/10
f=(int)(no-((h*100)+(p*50)+(t*20)+(te*10)))/5

print("100Rs",h)
print("50Rs",p)
print("20Rs",t)
print("10Rs",te)
print("5Rs",f)
        
