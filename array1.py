import array as arry
a=arry.array("i",[10,20,30,40,50])
b=arry.array("i",[15,25,35,45,55])

print(a)
print(b)

a.extend(b)
print(a)

c=sorted(a)
print(c)

c.reverse()
print(c)
